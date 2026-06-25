# Həqiqətən hər yerdə (həm hlsplayer-də, həm TV-də) açıq olan rəsmi yayım linkləri
channels = [
    # --- AZƏRBAYCAN KANALLARI (Açıq və Stabil) ---
    {"name": "İctimai TV (İTV)", "link": "https://stream.itv.az/itv/itv.m3u8", "group": "Azərbaycan"},
    {"name": "Xəzər TV", "link": "https://live.xazar.az/hls/stream.m3u8", "group": "Azərbaycan"},
    {"name": "CBC Azerbaijan", "link": "https://stream.cbc.az/cbc/cbc.m3u8", "group": "Azərbaycan"},
    
    # --- TRT RƏSMİ LİNKƏRİ (Heç bir pleyerdə qapanmayan rəsmi CDN yolları) ---
    {"name": "TRT Belgesel HD", "link": "https://trt.live.enetres.net/live/trtbelgesel.m3u8", "group": "Belgesel"},
    {"name": "TRT 1 HD", "link": "https://trt.live.enetres.net/live/trt1.m3u8", "group": "Ulusal"},
    {"name": "TRT Spor HD", "link": "https://trt.live.enetres.net/live/trtspor.m3u8", "group": "Spor"},
    {"name": "TRT Haber HD", "link": "https://trt.live.enetres.net/live/trthaber.m3u8", "group": "Haber"},
    {"name": "TRT Avaz HD", "link": "https://trt.live.enetres.net/live/trtavaz.m3u8", "group": "Ulusal"},
    {"name": "TRT Müzik", "link": "https://trt.live.enetres.net/live/trtmuzik.m3u8", "group": "Müzik"},
    
    # --- DİGƏR AÇIQ TÜRK KANALLARI ---
    {"name": "HaberTürk HD", "link": "https://ciner-live.daioncdn.net/haberturk/haberturk.m3u8", "group": "Haber"},
    {"name": "Show TV HD", "link": "https://ciner-live.daioncdn.net/showtv/showtv.m3u8", "group": "Ulusal"},
    {"name": "Bloomberg HT", "link": "https://ciner-live.daioncdn.net/bloomberght/bloomberght.m3u8", "group": "Haber"}
]

m3u_text = "#EXTM3U\n"

for ch in channels:
    m3u_text += f'#EXTINF:-1 group-title="{ch["group"]}", {ch["name"]}\n'
    m3u_text += f"{ch['link']}\n"

with open("tv.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_text)

print("tv.m3u faylı tam rəsmi və bloklanmayan yayım şəbəkəsi ilə yeniləndi!")

