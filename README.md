
# Video Translator Subtitles Application

## Setup Instructions (Windows VM)

1. Install **Python 3.11+** and **FFmpeg** (add FFmpeg to PATH).
2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Replace keys in `app.py` with your Azure Speech & Translator keys.
4. Run the application:

```powershell
python app.py
```

5. Open a browser and navigate to:

```
http://<VM_PUBLIC_IP>:5000
```

6. Optional: Embed subtitles into video using FFmpeg:

```powershell
ffmpeg -i input.mp4 -vf subtitles=subtitles.srt output.mp4
```
