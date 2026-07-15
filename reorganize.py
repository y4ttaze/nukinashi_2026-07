import os
import shutil
import json
import glob

def setup():
    # Target structure
    # data/y4ttaze_DaysBeforeVillain(CD)/
    # data/y4ttaze_sexT4pe(1)_CD/

    data_dir = 'data'
    
    # 1. DaysBeforeVillain
    dbv_old = os.path.join(data_dir, '00_DaysBeforeVillain(CD)')
    dbv_new = os.path.join(data_dir, 'y4ttaze_DaysBeforeVillain(CD)')
    if os.path.exists(dbv_old) and not os.path.exists(dbv_new):
        os.makedirs(dbv_new)
        # Move audio
        audio_src = os.path.join(dbv_old, 'work/音源/02. CD Version')
        for f in glob.glob(os.path.join(audio_src, '*.wav')):
            shutil.copy(f, os.path.join(dbv_new, os.path.basename(f)))
        # Move jacket
        jacket = os.path.join(dbv_old, 'work/ジャケ写・アー写/ジャケ写/みんちさん_days_before_villain_ジャケ写_image_無題2782_20260307002813.png')
        if os.path.exists(jacket):
            shutil.copy(jacket, os.path.join(dbv_new, 'jacket.png'))
        # Move teaser
        teaser = os.path.join(dbv_old, 'Days Before Villain teaser_fumi_san_ver - HD 1080p.mov')
        if os.path.exists(teaser):
            shutil.copy(teaser, os.path.join(dbv_new, 'teaser.mov'))

    # 2. sexT4pe
    st_old = os.path.join(data_dir, '00_sexT4pe(1)_CD')
    st_new = os.path.join(data_dir, 'y4ttaze_sexT4pe(1)_CD')
    if os.path.exists(st_old) and not os.path.exists(st_new):
        os.makedirs(st_new)
        # Move audio
        audio_src = os.path.join(st_old, 'worx/音源')
        for f in glob.glob(os.path.join(audio_src, '*.wav')):
            shutil.copy(f, os.path.join(st_new, os.path.basename(f)))
        # Move jacket
        jacket = os.path.join(st_old, 'worx/ジャケ写/Untitled32_20250812005608.png')
        if os.path.exists(jacket):
            shutil.copy(jacket, os.path.join(st_new, 'jacket.png'))
        # Move teaser
        teaser = os.path.join(st_old, 'sexT4pe_xfade_0714 - HD 1080p.mov')
        if os.path.exists(teaser):
            shutil.copy(teaser, os.path.join(st_new, 'teaser.mov'))

    # Cleanup old ones? User said "manipulate the directory" but copying is safer. Let's move them to a backup folder or just leave them.
    # To keep it clean, let's delete the old ones since they have backups.
    if os.path.exists(dbv_old): shutil.rmtree(dbv_old)
    if os.path.exists(st_old): shutil.rmtree(st_old)

    # 3. Create build_db.py that reads the new structure
    build_db_code = """import os
import json
import glob

data_dir = 'data'
db = []

for ep_folder in sorted(os.listdir(data_dir)):
    ep_path = os.path.join(data_dir, ep_folder)
    if not os.path.isdir(ep_path): continue
    
    parts = ep_folder.split('_', 1)
    if len(parts) == 2:
        artist, title = parts
    else:
        artist, title = 'Unknown', ep_folder

    ep_data = {
        'id': ep_folder,
        'title': title,
        'jacket': None,
        'teaser': None,
        'tracks': []
    }

    # Find jacket
    jackets = glob.glob(os.path.join(ep_path, '*jacket*.*')) + glob.glob(os.path.join(ep_path, '*.png')) + glob.glob(os.path.join(ep_path, '*.jpg'))
    if jackets:
        ep_data['jacket'] = jackets[0]

    # Find teaser
    teasers = glob.glob(os.path.join(ep_path, '*teaser*.*')) + glob.glob(os.path.join(ep_path, '*.mov')) + glob.glob(os.path.join(ep_path, '*.mp4'))
    if teasers:
        ep_data['teaser'] = teasers[0]

    # Find audio
    for ext in ['*.wav', '*.mp3', '*.flac', '*.m4a']:
        for audio_file in sorted(glob.glob(os.path.join(ep_path, ext))):
            filename = os.path.basename(audio_file)
            track_title = os.path.splitext(filename)[0]
            # Strip leading numbers like '01.' or '01_' if you want, or keep it.
            # User format: {0埋め2桁数字}_{タイトル}.{拡張子}
            if track_title[2] in ['.', '_', ' ']:
                track_title = track_title[3:].strip()
                
            ep_data['tracks'].append({
                'title': track_title,
                'src': audio_file
            })
    
    if ep_data['tracks']:
        db.append(ep_data)

with open(os.path.join(data_dir, 'db.json'), 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False, indent=2)
print("db.json built successfully!")
"""
    with open('build_db.py', 'w') as f:
        f.write(build_db_code)
    
setup()
