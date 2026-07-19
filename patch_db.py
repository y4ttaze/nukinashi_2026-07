import json

with open("data/db.json", "r", encoding="utf-8") as f:
    db = json.load(f)

# Add B13,14 prefix to existing items
for item in db:
    if "【配置" not in item.get("description", ""):
        item["description"] = f"【配置: B13,14】{item.get('description', '')}"

# New Compilations
new_items = [
  {
    "id": "comp_lucylove5",
    "artist": "LUCY LOVE records",
    "title": "LUCY LOVE records vol.5",
    "jacket": "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><rect width='100%' height='100%' fill='%23333'/><text x='50%' y='50%' font-size='24' fill='%23fff' text-anchor='middle' dy='.3em'>NO IMAGE</text></svg>",
    "artist_img": "",
    "teaser": "",
    "price": "¥1,000",
    "tracks_count": 15,
    "description": "【配置: B17,18】LUCY LOVE recordsさんのコンピ！カミナシ（Tr.04）、y4ttaze（Tr.08）が参加しています！",
    "tracks": [
      {"title": "夏の終わり - feat. 結月ゆかり / 螟上?陦ゆo繧"},
      {"title": "翡翠の華 - feat. AI ついなちゃん / 405人"},
      {"title": "Smell The Rat - 歌い手 / lev & ka7me"},
      {"title": "ずるやすみ - feat. AI 宮舞モカ / カミナシ"},
      {"title": "記憶 - feat. GUMI / 菅野"},
      {"title": "恋するワーカーホリック - feat. 可不 / nice_tack"},
      {"title": "カシス色の魔法 - feat. 音街ウナ / ななり"},
      {"title": "カルトちゃん - feat. NAKUMO / y4ttaze"},
      {"title": "悪手 - feat. 可不 / カルトちゃん"},
      {"title": "オメガフレア - feat. 松嘩りすく / ワタナベナオキ"},
      {"title": "No One Knows Me - feat. 重音テト / ヘルP"},
      {"title": "ストレリチヤ - feat. 宮舞モカ / 田淵フミ"},
      {"title": "CPH4 - feat. Ci flower, 花隈千冬 / 小出憂鬱"},
      {"title": "道化 - Instrumental / 泣き缶"},
      {"title": "自孤愛賛歌 - feat. MAYU / ヘイテートP"}
    ]
  },
  {
    "id": "comp_hiphop",
    "artist": "HipHop コンピ",
    "title": "合成音声x HipHop コンピ",
    "jacket": "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><rect width='100%' height='100%' fill='%23333'/><text x='50%' y='50%' font-size='24' fill='%23fff' text-anchor='middle' dy='.3em'>NO IMAGE</text></svg>",
    "artist_img": "",
    "teaser": "",
    "price": "¥2,500",
    "tracks_count": 15,
    "description": "【配置: B04】合成音声×HipHopコンピレーション！y4ttaze（Tr.11）が参加しています！",
    "tracks": [
      {"title": "モ葛 - No Lie ~マジのガチで~"},
      {"title": "呆 - 寿司が食べたい"},
      {"title": "夜行梅 - 薫陶"},
      {"title": "安見すや - おくのグリッチ"},
      {"title": "B9☆ - HANAKO"},
      {"title": "背面8回宙返り_イズム feat. d.j.ァネイロ"},
      {"title": "appy - 年輪"},
      {"title": "音無あふ - 四国中央ポップ"},
      {"title": "ikomai - ネオ体幹"},
      {"title": "Mi7s3 - CRACK!!"},
      {"title": "y4ttaze - マゼンタ"},
      {"title": "佐藤語幸 & Helwi_ - わかってない"},
      {"title": "misainthedxrk - SMOG!"},
      {"title": "駱駝法師 & M4tt - RUMAKINCLASSIC"},
      {"title": "chickendream - crankup"}
    ]
  },
  {
    "id": "comp_nina12",
    "artist": "niña",
    "title": "niña vol.12",
    "jacket": "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><rect width='100%' height='100%' fill='%23333'/><text x='50%' y='50%' font-size='24' fill='%23fff' text-anchor='middle' dy='.3em'>NO IMAGE</text></svg>",
    "artist_img": "",
    "teaser": "",
    "price": "¥270",
    "tracks_count": 15,
    "description": "【配置: C58】niña vol.12！y4ttaze（Tr.03）が参加しています！",
    "tracks": [
      {"title": "或る朝、私は私を裏切る / ニルアドミラリ"},
      {"title": "仄暗い天井裏からあなたに傘を差しに来ました。/ テレキャス欲し夫"},
      {"title": "みるく / y4ttaze"},
      {"title": "余生活 / 小出憂鬱"},
      {"title": "さがしごと、ねがいごと / Love-Ghost-Lab!"},
      {"title": "少女の詩 / 故やす子"},
      {"title": "Girls Who Never Became Girls / 村前銘紗"},
      {"title": "私は私 / HIYARI-HAT"},
      {"title": "愛がないぜ / 田淵フミ"},
      {"title": "E.G.Rider / 猿楽雅"},
      {"title": "花火と月 / でんぽん"},
      {"title": "褥音 / Mocker"},
      {"title": "Bluebell / アルシャトP"},
      {"title": "人喰花 / プチヒコ"},
      {"title": "鬼姫 / はまたい"}
    ]
  },
  {
    "id": "comp_nina11",
    "artist": "niña",
    "title": "niña vol.11 (旧譜)",
    "jacket": "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><rect width='100%' height='100%' fill='%23333'/><text x='50%' y='50%' font-size='24' fill='%23fff' text-anchor='middle' dy='.3em'>NO IMAGE</text></svg>",
    "artist_img": "",
    "teaser": "",
    "price": "¥270",
    "tracks_count": 16,
    "description": "【配置: C58】niña vol.11 (旧譜)。y4ttaze（Tr.01）、カミナシ（Tr.14）が参加しています！",
    "tracks": [
      {"title": "AKB48 / y4ttaze"},
      {"title": "サムワンズノウ（加納先生）/ 包丁ナイフカッターズ"},
      {"title": "おやすみ開戦前夜 / ロクガツ"},
      {"title": "空想の美少女 / チームひややっこセット"},
      {"title": "スカルのネイル / まねきぼうず"},
      {"title": "スモールトーク / 小出憂鬱"},
      {"title": "センリツガールとファズ構文 / 志乃々芽らいか"},
      {"title": "たたかわない女の子 / うしみつ3"},
      {"title": "Sugoku Darakushita Girl's / 猿楽雅"},
      {"title": "嘘がある/ 𓂍𓂌えむえぬ"},
      {"title": "月影の唄 / けいち"},
      {"title": "That Girl / Ranze"},
      {"title": "君は夜に染まって / カミヰユウ"},
      {"title": "海の月 / カミナシ"},
      {"title": "Moonlight / ミヤ=A"},
      {"title": "憧憬の果て / なまにく"}
    ]
  }
]

db.extend(new_items)

with open("data/db.json", "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print("Patch complete.")
