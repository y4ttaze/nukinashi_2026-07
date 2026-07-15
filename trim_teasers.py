import os
import subprocess
from glob import glob

def run_cmd(cmd):
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

def trim_videos():
    vid_files = glob("data/**/*.mp4", recursive=True) + glob("data/**/*.mov", recursive=True)
    for vid in vid_files:
        # We want to trim to 30s and add a fade-out from 28s to 30s
        out_vid = vid.rsplit(".", 1)[0] + "_trimmed.mp4"
        if not os.path.exists(out_vid):
            cmd = [
                "ffmpeg", "-i", vid,
                "-t", "30",
                "-vf", "fade=t=out:st=28:d=2",
                "-af", "afade=t=out:st=28:d=2",
                "-c:v", "libx264", "-crf", "28", "-preset", "veryfast",
                "-c:a", "aac", "-b:a", "128k",
                "-y", out_vid
            ]
            try:
                run_cmd(cmd)
                os.remove(vid)
                os.rename(out_vid, vid.rsplit(".", 1)[0] + ".mp4")
            except Exception as e:
                print(f"Failed {vid}: {e}")

if __name__ == "__main__":
    trim_videos()
