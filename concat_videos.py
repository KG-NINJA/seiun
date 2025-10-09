from moviepy.editor import VideoFileClip, concatenate_videoclips
import json, os

def load_config(path="video_config.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def build_clip(segment):
    clip = VideoFileClip(segment["file"]).subclip(0, segment.get("duration", None))
    trans = segment.get("transition")
    if trans == "fadein":
        clip = clip.fadein(1)
    elif trans == "fadeout":
        clip = clip.fadeout(1)
    elif trans == "crossfade":
        clip = clip.crossfadein(1)
    return clip

def concat_videos(cfg):
    clips = [build_clip(seg) for seg in cfg["segments"]]
    final = concatenate_videoclips(clips, method="compose")
    os.makedirs(os.path.dirname(cfg["global_settings"]["output_file"]), exist_ok=True)
    final.write_videofile(cfg["global_settings"]["output_file"], fps=cfg["global_settings"]["fps"])

if __name__ == "__main__":
    cfg = load_config()
    concat_videos(cfg)
    print("✅ Final video created:", cfg["global_settings"]["output_file"])
