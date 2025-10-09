# 🎬 SoraConcatStudio
Combine multiple **Sora-generated video scenes** into a seamless short film using Python.

### 🚀 Usage
1. Place Sora videos inside `/videos`
2. Edit `video_config.json` to define order and transitions
3. Run:
   ```bash
   python concat_videos.py
   ```
4. Output → `output/final_video.mp4`

### 💡 Requirements
- Python 3.10+
- moviepy (`pip install moviepy`)

### 🌈 Optional Extensions
- Add audio track (`AudioFileClip`)
- Overlay subtitles (requires ImageMagick)
- Trigger automation via GitHub Actions
