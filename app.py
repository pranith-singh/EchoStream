from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
import os
from azure.storage.blob import BlobServiceClient
import whisper
from deep_translator import GoogleTranslator
from waitress import serve

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Azure Blob storage config
STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=**;AccountKey=********"
STORAGE_ACCOUNT_NAME = "prs"
CONTAINER_NAME = "files"
blob_service_client = BlobServiceClient.from_connection_string(STORAGE_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

# Local uploads folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Supported subtitle languages
LANGUAGES = ["English", "Telugu", "Hindi", "Tamil"]

# Whisper model
model = whisper.load_model("base")

# ----------------- ROUTES -----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "admin":
            session["logged_in"] = True
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route("/index", methods=["GET"])
def index():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    if "video" not in request.files:
        return "No file part", 400

    file = request.files["video"]
    if file.filename == "":
        return "No selected file", 400

    filename = secure_filename(file.filename)
    local_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(local_path)

    # Upload to Azure Blob
    with open(local_path, "rb") as data:
        container_client.upload_blob(name=filename, data=data, overwrite=True)

    os.remove(local_path)
    return redirect(url_for("watch", video_name=filename))

@app.route("/watch/<video_name>", methods=["GET"])
def watch(video_name):
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    video_url = f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net/{CONTAINER_NAME}/{video_name}"

    # Download blob temporarily
    local_temp = os.path.join(UPLOAD_FOLDER, video_name)
    with open(local_temp, "wb") as f:
        blob_data = container_client.download_blob(video_name)
        blob_data.readinto(f)

    # Generate subtitles
    result = model.transcribe(local_temp)
    text = result["text"]

    subtitles = {}
    for lang in LANGUAGES:
        if lang == "English":
            subtitles[lang] = text
        else:
            try:
                subtitles[lang] = GoogleTranslator(source='auto', target=lang[:2].lower()).translate(text)
            except Exception as e:
                subtitles[lang] = f"Translation error: {str(e)}"

    os.remove(local_temp)
    return render_template("watch.html", subtitles=subtitles, languages=LANGUAGES, video_url=video_url)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# ----------------- START SERVER -----------------
if __name__ == "__main__":
    print("Starting Waitress on 0.0.0.0:8080")
    serve(app, host="0.0.0.0", port=8080)
