# -*- coding: utf-8 -*-
""" Series information for each label.
"""
from label_translate import label_to_japanese, label_to_english

series = {
    "Touhou Project": [
        u"レミリア・スカーレット",
        u"諏訪子",
        u"鍵山雛",
        u"魂魄妖夢",
        u"フランドール・スカーレット",
        u"てゐ",
        u"お空",
        u"八雲紫",
        u"紅美鈴",
        u"伊吹萃香",
        u"小悪魔",
        u"犬走椛",
        u"古明地さとり",
        u"射命丸文",
        u"西行寺幽々子",
        u"うどんげ",
        u"チルノ",
        u"十六夜咲夜",
        u"大妖精",
        u"ルーミア",
        u"パチュリー",
        u"東風谷早苗",
        u"藤原妹紅",
        u"風見幽香",
        u"比那名居天子",
        u"寅丸星",
        u"ナズーリン",
        u"古明地こいし",
        u"水橋パルスィ",
        u"八雲藍",
        u"橙",
        u"博麗霊夢",
        u"封獣ぬえ",
        u"アリス・マーガトロイド",
        u"魔理沙"
    ],
    "Vocaloid": [
        u"KAITO",
        u"鏡音リン",
        u"巡音ルカ",
        u"神威がくぽ",
        u"初音ミク",
        u"MEIKO",
        u"鏡音レン"
    ],
    "Free!": [
        u"松岡凛",
        u"橘真琴",
        u"七瀬遙"
    ],
    "Kagerou Project": [
        u"シンタロー",
        u"アヤノ",
        u"カノ"
    ],
    "Gin Tama": [
        u"沖田総悟",
        u"神楽",
        u"土方十四郎",
        u"高杉晋助",
        u"坂田銀時"
    ],
    "Pokémon": [
        u"ピカチュウ"
    ],
    "Hoozuki no Reitetsu": [
        u"鬼灯",
        u"白澤"
    ],
    "Attack on Titan": [
        u"エレン・イェーガー",
        u"ミカサ・アッカーマン",
        u"リヴァイ"
    ],
    "Kuroko's Basketball": [
        u"高尾和成",
        u"赤司征十郎",
        u"緑間真太郎",
        u"黒子テツヤ",
        u"青峰大輝",
        u"黄瀬涼太",
        u"火神大我",
        u"紫原敦"
    ],
    "Puella Magi Madoka Magica": [
        u"暁美ほむら",
        u"鹿目まどか",
        u"巴マミ",
        u"佐倉杏子",
        u"キュゥべえ",
        u"美樹さやか"
    ],
    "Sengoku Basara": [
        u"真田幸村",
        u"長曾我部元親",
        u"毛利元就",
        u"石田三成",
        u"徳川家康",
        u"伊達政宗"
    ],
    "Magi: The Labyrinth of Magic": [
        u"アラジン",
        u"アリババ"
    ],
    "Hetalia: Axis Powers": [
        u"ルートヴィッヒ",
        u"ロヴィーノ・ヴァルガス",
        u"イヴァン・ブラギンスキ",
        u"フェリシアーノ・ヴァルガス",
        u"アルフレッド・F・ジョーンズ",
        u"ギルベルト・バイルシュミット",
        u"アントーニョ・ヘルナンデス・カリエド",
        u"本田菊",
        u"アーサー・カークランド",
        u"王耀",
        u"フランシス・ボヌフォワ"
    ],
    "One Piece": [
        u"ゾロ",
        u"トラファルガー・ロー",
        u"サンジ",
        u"ルフィ"
    ],
    "K-On!": [
        u"平沢唯",
        u"中野梓",
        u"秋山澪",
        u"田井中律"
    ],
    "Blue Exorcist": [
        u"奥村燐"
    ],
    "Inazuma Eleven GO": [
        u"霧野蘭丸"
    ],
    "The Idolmaster": [
        u"天海春香",
        u"菊地真"
    ],
    "Neon Genesis Evangelion": [
        u"碇シンジ",
        u"渚カヲル"
    ],
    "Durarara!!": [
        u"折原臨也",
        u"平和島静雄"
    ],
    "Tiger & Bunny": [
        u"バーナビー・ブルックスJr.",
        u"鏑木・T・虎徹"
    ],
    "Uta no Prince-sama": [
        u"美風藍",
        u"来栖翔"
    ],
    "Love Live!": [
        u"矢澤にこ"
    ],
    "Kantai Collection": [
        u"島風"
    ],
    "Fate/Stay night": [
        u"セイバー"
    ]
}

# Localization of series names in English and Japanese.
# English names are just the original names.
series_en = {}

for name in series:
    series_en[name] = name.decode('utf-8')

# Manually translated Japanese names.
series_ja = {
    "Touhou Project": u"東方Project",
    "Vocaloid": u"ボーカロイド",
    "Free!": u"Free!",
    "Kagerou Project": u"カゲロウプロジェクト",
    "Gin Tama": u"銀魂",
    "Hoozuki no Reitetsu": u"鬼灯の冷徹",
    "Attack on Titan": u"進撃の巨人",
    "Kuroko's Basketball": u"黒子のバスケ",
    "Puella Magi Madoka Magica": u"魔法少女まどか☆マギカ",
    "Sengoku Basara": u"戦国BASARA",
    "Magi: The Labyrinth of Magic": u"マギ",
    "Hetalia: Axis Powers": u"ヘタリア Axis Powers",
    "One Piece": u"ワンピース",
    "K-On!": u"けいおん!",
    "Blue Exorcist": u"青の祓魔師",
    "Inazuma Eleven GO": u"イナズマイレブン GO",
    "The Idolmaster": u"アイドルマスター",
    "Neon Genesis Evangelion": u"新世紀エヴァンゲリオン",
    "Durarara!!": u"デュラララ!!",
    "Tiger & Bunny": u"タイガー＆バニー",
    "Uta no Prince-sama": u"うたの☆プリンスさまっ♪",
    "Love Live!": u"ラブライブ!",
    "Kantai Collection": u"艦隊これくしょん",
    "Fate/Stay night": u"フェイト/ステイナイト",
    "Pokémon": u"ポケモン"
}

def translated_chars(locale):
    series_trans = None
    char_trans = None
    if locale == 'en':
        series_trans = series_en
        char_trans = label_to_english
    elif locale == 'ja':
        series_trans = series_ja
        char_trans = label_to_japanese
    else:
        raise ValueError("Invalid locale: " + repr(locale))

    chars = {}

    for sname in series:
        sname_u = series_trans[sname]
        chars[sname_u] = []
        for char in series[sname]:
            chars[sname_u].append(char_trans[char])

    return chars
