import os
import json
import glob

data_dir = 'data'
db = []
original_db = []

# Load original DB if it exists
try:
    with open(os.path.join('..', '即売会_視聴アプリ', 'data', 'db.json'), 'r', encoding='utf-8') as f:
        original_db = json.load(f)
except Exception as e:
    print(f"Warning: Could not load original db.json: {e}")

current_db = []
try:
    with open(os.path.join(data_dir, 'db.json'), 'r', encoding='utf-8') as f:
        current_db = json.load(f)
except Exception:
    pass

for ep_folder in sorted(os.listdir(data_dir)):
    ep_path = os.path.join(data_dir, ep_folder)
    if not os.path.isdir(ep_path): continue
    
    parts = ep_folder.split('_', 2)
    if len(parts) >= 3:
        prefix, artist, title = parts[0], parts[1], parts[2]
    elif len(parts) == 2:
        artist, title = parts
    else:
        artist, title = 'Unknown', ep_folder

    ep_data = {
        'id': ep_folder,
        'artist': artist,
        'title': title,
        'jacket': None,
        'artist_img': None,
        'teaser': None,
        'tracks': []
    }

    # Find jacket
    jackets = glob.glob(os.path.join(ep_path, '*jacket*.*')) + glob.glob(os.path.join(ep_path, '*.png')) + glob.glob(os.path.join(ep_path, '*.jpg')) + glob.glob(os.path.join(ep_path, '*.webp'))
    
    # Filter out artist.* from jackets fallback
    jackets = [j for j in jackets if not os.path.basename(j).lower().startswith('artist.')]
    if jackets:
        ep_data['jacket'] = jackets[0]

    # Find artist image
    artist_imgs = glob.glob(os.path.join(ep_path, 'artist*.*')) + glob.glob(os.path.join(data_dir, f'artist*_{artist}.*'))
    if artist_imgs:
        img_path = artist_imgs[0]
        ep_data['artist_img'] = img_path
        # Extract artist name from artist_NAME.ext if present
        base_name = os.path.basename(img_path)
        name_part = os.path.splitext(base_name)[0]
        if '_' in name_part:
            extracted_name = name_part.split('_', 1)[1]
            if extracted_name:
                ep_data['artist'] = extracted_name

    # Find teaser
    teasers = glob.glob(os.path.join(ep_path, '*teaser*.*')) + glob.glob(os.path.join(ep_path, '*.mov')) + glob.glob(os.path.join(ep_path, '*.mp4'))
    if teasers:
        ep_data['teaser'] = teasers[0]

    # Since we deleted audio files in this directory, we fetch tracks from the original DB.
    # We find the matching EP by 'id' loosely or by 'title'
    original_ep = next((ep for ep in original_db if ep_folder.startswith(ep['id']) or ep['title'] == title), None)
    
    if original_ep and 'tracks' in original_ep:
        # We don't actually need the src, just the titles for the catalog, but we keep the same structure
        ep_data['tracks'] = original_ep['tracks']

    # Preserve manually added keys from the current db.json
    current_ep = next((ep for ep in current_db if ep['id'] == ep_folder), None)
    if current_ep:
        for key in ['tracks', 'x', 'yt', 'nico', 'price', 'description', 'tracks_count']:
            if key in current_ep:
                ep_data[key] = current_ep[key]

    # Strip out 'src' for security
    if 'tracks' in ep_data:
        clean_tracks = []
        for t in ep_data['tracks']:
            clean_tracks.append({"title": t.get("title", "")})
        ep_data['tracks'] = clean_tracks

    # Read optional info.json (overrides current_db)
    info_path = os.path.join(ep_path, 'info.json')
    if os.path.exists(info_path):
        with open(info_path, 'r', encoding='utf-8') as f:
            try:
                info = json.load(f)
                ep_data['price'] = info.get('price', ep_data.get('price', '¥1,000'))
                ep_data['tracks_count'] = info.get('tracks_count', ep_data.get('tracks_count', len(ep_data['tracks'])))
                ep_data['description'] = info.get('description', ep_data.get('description', '最新作！'))
            except:
                pass
    
    if 'price' not in ep_data:
        ep_data['price'] = '¥1,000'
        ep_data['tracks_count'] = len(ep_data['tracks'])
        ep_data['description'] = '最新作！'
    
    # We no longer require audio tracks for the catalog
    db.append(ep_data)

with open(os.path.join(data_dir, 'db.json'), 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False, indent=2)
print("db.json built successfully!")
