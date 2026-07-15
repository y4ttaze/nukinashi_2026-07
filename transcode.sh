#!/bin/bash
SRC_DIR="/Users/mac/Desktop/アプリ作りたい/即売会_視聴アプリ/data"
DEST_DIR="/Users/mac/Desktop/アプリ作りたい/即売会_デジタルお品書き/data"

echo "Processing 01..."
ffmpeg -y -i "$SRC_DIR/01_y4ttaze_DaysBeforeVillain/teaser.mov" -c:v libx264 -preset fast -crf 23 -c:a aac -b:a 128k "$DEST_DIR/01_y4ttaze_DaysBeforeVillain(CD)/teaser.mp4"

echo "Processing 02..."
ffmpeg -y -i "$SRC_DIR/02_y4ttaze_sexT4pe/teaser.mov" -c:v libx264 -preset fast -vf "scale=-2:720" -crf 32 -c:a aac -b:a 128k "$DEST_DIR/02_y4ttaze_sexT4pe(1)_CD/teaser.mp4"

echo "Processing 03..."
ffmpeg -y -i "$SRC_DIR/03_カミナシ_孤独なテラリウム/XFD.mp4" -c:v libx264 -preset fast -vf "scale=-2:720" -crf 32 -c:a aac -b:a 128k "$DEST_DIR/03_カミナシ_孤独なテラリウム/XFD.mp4"

echo "Processing 04..."
cp "$SRC_DIR/04_雨花_雨の降る街で。/Teaser.mp4" "$DEST_DIR/04_雨花_雨の降る街で。/Teaser.mp4"

echo "Done!"
