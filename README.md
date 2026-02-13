
<p align="center">
  <img src="static/logo.png" alt="EchoStream Logo" width="140" />
</p>

# 🔊 EchoStream

**Cloud‑powered audio translation** to Telugu, Hindi, and Tamil with automatic storage in **Azure Blob Storage** or **AWS S3**.

[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ff69b4?logo=github)](https://github.com/sponsors/praniith-singh)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](#)
[![Framework](https://img.shields.io/badge/Flask-2.x-000?logo=flask)](#)
[![Azure Blob](https://img.shields.io/badge/Storage-Azure%20Blob-0078D4?logo=microsoft-azure&logoColor=white)](#)
[![AWS S3](https://img.shields.io/badge/Storage-AWS%20S3-232F3E?logo=amazon-aws&logoColor=white)](#)
[![Stars](https://img.shields.io/github/stars/praniith-singh/echostream?style=social)](https://github.com/praniith-singh/echostream/stargazers)

> **Tagline:** *Bridge your voice to any language — securely, at cloud scale.*

---

## 📖 Overview
EchoStream takes an audio file (e.g., WAV/MP3), performs **speech → translation** into **Telugu (te)**, **Hindi (hi)**, or **Tamil (ta)**, and persists results and artifacts to your chosen cloud storage (**Azure Blob** or **AWS S3**). A simple web UI and REST API are included so you can automate the workflow or use it manually.

---

## ✨ Features
- 🎙️ **Audio in → Multilingual out** (Telugu, Hindi, Tamil)
- ⚡ **Batch or single uploads** via REST API or Web UI
- ☁️ **Pluggable storage**: Azure Blob or AWS S3
- 🔐 **Secure by default**: environment‑based secrets (no keys in code)
- 🧩 **Modular pipeline**: swap STT/translation providers as needed
- 📦 **Container‑ready** and deployable to Azure App Service / AWS

---

## 🧱 Architecture (High level)
```
[Client/UI or cURL]
        │  POST /api/v1/translate (audio, target_lang)
        ▼
   Flask API (app.py)
        │
        ├─ Transcribe (provider of your choice)
        │
        ├─ Translate → te | hi | ta
        │
        └─ Store → Azure Blob  OR  AWS S3
                         │
                         └─ Return JSON (status + storage URL)
```

---

## 🚀 Quickstart

### 1) Clone
```bash
git clone https://github.com/praniith-singh/echostream.git
cd echostream
```

### 2) Create & activate a virtual environment
```bash
python -m venv venv
# Mac/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3) Install dependencies
```bash
pip install -r requirements.txt
```

### 4) Configure environment
Create a **.env** file in the project root:

```env
# Choose: azure | aws
CLOUD_PROVIDER=azure

# --- Azure Blob Storage ---
AZURE_STORAGE_CONNECTION_STRING="<your-connection-string>"
AZURE_BLOB_CONTAINER="echostream"

# --- AWS S3 ---
AWS_ACCESS_KEY_ID="<your-access-key>"
AWS_SECRET_ACCESS_KEY="<your-secret>"
AWS_DEFAULT_REGION="ap-south-1"
AWS_S3_BUCKET="echostream"

# --- Speech & Translation provider keys (optional placeholders) ---
# For example, if you wire Azure Cognitive Services or AWS Transcribe/Translate
AZURE_SPEECH_KEY="<if-using-azure-speech>"
AZURE_SPEECH_REGION="<region>"
AWS_TRANSCRIBE_REGION="ap-south-1"
AWS_TRANSLATE_REGION="ap-south-1"
```

> 📝 *Only set the variables for the cloud/provider you actually use.*

### 5) Run the app
```bash
python app.py
```
Open http://127.0.0.1:5000/

---

## 🔌 REST API

### `POST /api/v1/translate`
**Request (multipart/form-data):**
- `file`: audio file (e.g., .wav, .mp3)
- `target_lang`: one of `te`, `hi`, `ta`

**cURL example:**
```bash
curl -X POST http://127.0.0.1:5000/api/v1/translate   -F "file=@samples/hello.mp3"   -F "target_lang=te"
```

**Response (example):**
```json
{
  "id": "c4f0...",
  "language": "te",
  "status": "completed",
  "storage_provider": "azure",
  "artifact_url": "https://.../echostream/outputs/c4f0.../translation.json"
}
```

### `GET /api/v1/health`
Basic health check endpoint.

---

## 🗄️ Storage Configuration

### Azure Blob
- Provide `AZURE_STORAGE_CONNECTION_STRING` and `AZURE_BLOB_CONTAINER`.
- Container will be created if it doesn't exist (recommended name: `echostream`).

### AWS S3
- Provide `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_DEFAULT_REGION`, and `AWS_S3_BUCKET`.
- Bucket should exist; app can create folders/prefixes per job.

> 🔒 Manage secrets via environment variables locally and via your cloud's configuration (Azure App Service settings / AWS Elastic Beanstalk or ECS task definitions).

---

## 🧪 Local Dev Tips
- Install **ffmpeg** if you need robust audio handling.
- Keep sample audio in `samples/` to test quickly.
- Use `.env` and avoid committing secrets.

---

## 🌐 Deployment

### Azure App Service
1. Push the repo to GitHub.
2. Create **App Service → Python**.
3. Connect Deployment Center to this repo/branch.
4. In **Configuration → Application settings**, add the environment variables shown above.
5. Redeploy.

### AWS (one option)
- Use **Elastic Beanstalk (Python)** or containerize and deploy via **ECS/Fargate**.
- Set env vars in the service configuration.

---

## 🛣️ Roadmap
- Add diarization + speaker labels
- Add subtitle (SRT/VTT) export
- Add more Indic languages (bn, kn, ml, mr)
- Add async job queue for large files

---

## 🤝 Contributing
PRs are welcome! Please open an issue first to discuss major changes.

---

## ❤️ Sponsors
If you find this project useful, please consider sponsoring my work.

[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ff69b4?logo=github)](https://github.com/sponsors/praniith-singh)

> *Note: The Sponsor page will be live once GitHub approves the application.*

---

## 📜 License
MIT License — see **LICENSE** for details.
