import os
import subprocess
from glob import glob

def run_cmd(cmd):
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

def optimize_audio():
    wav_files = glob("data/**/*.wav", recursive=True)
    for wav in wav_files:
        mp3_out = wav.rsplit(".", 1)[0] + ".mp3"
        if not os.path.exists(mp3_out):
            # Compress to V0 VBR MP3 (very high quality, but small)
            cmd = ["ffmpeg", "-i", wav, "-q:a", "0", "-map_metadata", "0", "-y", mp3_out]
            try:
                run_cmd(cmd)
                print(f"Removing original wav: {wav}")
                os.remove(wav)
            except Exception as e:
                print(f"Failed to convert {wav}: {e}")

def optimize_images():
    # Convert PNG to optimized JPG or WEBP (WEBP is better for web)
    img_files = glob("data/**/*.png", recursive=True) + glob("data/**/*.jpg", recursive=True)
    for img in img_files:
        webp_out = img.rsplit(".", 1)[0] + ".webp"
        if not os.path.exists(webp_out) and img != webp_out:
            # -lossless 0 -q 80 for reasonable compression
            cmd = ["ffmpeg", "-i", img, "-c:v", "libwebp", "-quality", "80", "-y", webp_out]
            try:
                run_cmd(cmd)
                print(f"Removing original image: {img}")
                os.remove(img)
            except Exception as e:
                print(f"Failed to convert {img}: {e}")

if __name__ == "__main__":
    print("Starting optimization...")
    optimize_audio()
    optimize_images()
    print("Optimization complete!")
    print("Rebuilding database...")
    run_cmd(["python3", "build_db.py"])
