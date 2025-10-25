from celery import Celery
import whisper
from googletrans import Translator
import os
from azure.storage.blob import BlobServiceClient
import json

UPLOAD_FOLDER = "uploads"
SUBTITLE_FOLDER = "subtitles"

# Celery config
celery = Celery('tasks', broker='redis://localhost:6379/0')

# Azure Blob
STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=prs;AccountKey=dyLZnt/CXmXMFV3YsPCaVrpHMgtmbDOH0hcursSRqJeVd1f1wS9d4bOLsfkj38mmOHJC2EOVrALp+AStexiNTw==;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "files"
blob_service_client = BlobServiceClient.from_connection_string(STORAGE_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

# Load Whisper model (tiny = fast)
model = whisper.load_model("tiny")
translator = Translator()
LANGUAGES = ["English", "Telugu", "Hindi", "Tamil"]

@celery.task
def generate_subtitles_task(filename):
    local_path = os.path.join(UPLOAD_FOLDER, filename)

    # Download blob temporarily
    with open(local_path, "wb") as f:
        blob_data = container_client.download_blob(filename)
        blob_data.readinto(f)

    # Transcribe
    result = model.transcribe(local_path)
    text = result["text"]

    # Translate to other languages
    subtitles = {}
    for lang in LANGUAGES:
        if lang == "English":
            subtitles[lang] = text
        else:
            translated = translator.translate(text, dest=lang.lower()).text
            subtitles[lang] = translated

    # Save subtitles JSON
    subtitles_path = os.path.join(SUBTITLE_FOLDER, f"{filename}.json")
    with open(subtitles_path, "w", encoding="utf-8") as f:
        json.dump(subtitles, f, ensure_ascii=False)

    os.remove(local_path)
