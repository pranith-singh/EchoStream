<p align="center">
  static/logo.png
</p>

<h1 align="center">EchoStream</h1>
<p align="center"><i>Bridge your voice to any language — securely, at cloud scale.</i></p>

<p align="center">
  <a href="https://github.com/sponsors/praniith-singh"><img alt="Sponsor" src="https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ff69b4?logo=github"></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-blue">
  <img alt="Flask" src="https://img.shields.io/badge/Flask-2.x-000?logo=flask">
  <img alt="Azure Blob" src="https://img.shields.io/badge/Storage-Azure%20Blob-0078D4?logo=microsoft-azure&logoColor=white">
  <img alt="AWS S3" src="https://img.shields.io/badge/Storage-AWS%20S3-232F3E?logo=amazon-aws&logoColor=white">
  <a href="https://github.com/praniith-singh/EchoStream/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/praniith-singh/EchoStream?style=social"></a>
</p>

---

## Overview
**EchoStream** converts uploaded audio (WAV/MP3) into **Telugu (te)**, **Hindi (hi)**, or **Tamil (ta)** and persistently stores results in **Azure Blob Storage** or **AWS S3**. Use a minimal **Web UI** for quick runs or the **REST API** to automate your translation workflows.

- ⚙️ **Built with:** Python (Flask)
- ☁️ **Storage targets:** Azure Blob, AWS S3
- 🌍 **Focus:** Indian languages for real‑world scenarios (support lines, field ops, learning)

---

## Why EchoStream?
Organizations in India and beyond need accurate, quick **audio‑to‑text translation** for regional languages. EchoStream reduces manual effort for:
- Customer support call summaries (te/hi/ta)
- Field interviews & research recordings
- Classroom/lecture captures in local languages
- Localized knowledge bases & subtitles

---

## Features
- 🎙️ **Audio → Translation** for **Telugu, Hindi, Tamil**
- 🔌 **REST API** & **simple Web UI**
- ☁️ **Pluggable storage**: Azure Blob or AWS S3
- 🔐 **Secrets via environment** (no keys in code)
- 🧩 **Modular pipeline** (swap STT/translation providers later)
- 🚀 **Ready to deploy** (Azure App Service / AWS)

---

## Quickstart

```bash
git clone https://github.com/praniith-singh/EchoStream.git
cd EchoStream
python -m venv venv
# Mac/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
pip install -r requirements.txt
