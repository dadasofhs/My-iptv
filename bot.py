# Hər hansı bir saytı skan etməyə ehtiyac yoxdur, birbaşa rəsmi və açıq IP-ləri yazırıq
channels = [
    # --- SƏNƏDLİ FİLM (BELGESEL) ---
    {"name": "TRT Belgesel HD", "link": "https://trt.canlitvme.com/trtbelgesel/trtbelgesel/playlist.m3u8", "group": "Belgesel"},
    {"name": "DMAX HD (Yedek)", "link": "https://cdn508.canlitvme.com/dmax/dmax/playlist.m3u8", "group": "Belgesel"},
    {"name": "TLC HD (Yedek)", "link": "https://cdn508.canlitvme.com/tlc/tlc/playlist.m3u8", "group": "Belgesel"},

    # --- ÜMUMİ KANALLAR ---
    {"name": "TRT 1 HD", "link": "https://trt.canlitvme.com/trt1/trt1/playlist.m3u8", "group": "Ulusal"},
    {"name": "ATV HD", "link": "https://atv.canlitvme.com/atv/atv/playlist.m3u8", "group": "Ulusal"},
    {"name": "Kanal D HD", "link": "https://kanald.canlitvme.com/kanald/kanald/playlist.m3u8", "group": "Ulusal"},
    {"name": "Star TV HD", "link": "https://star.canlitvme.com/star/star/playlist.m3u8", "group": "Ulusal"},
    {"name": "Show TV HD", "link": "https://show.canlitvme.com/show/show/playlist.m3u8", "group": "Ulusal"},
    {"name": "TV8 HD", "link": "https://tv8.canlitvme.com/tv8/tv8/playlist.m3u8", "group": "Ulusal"},

    # --- İDMAN VƏ XƏBƏR ---
    {"name": "TRT Spor HD", "link": "https://trt.canlitvme.com/trtspor/trtspor/playlist.m3u8", "group": "Spor"},
    {"name": "A Spor HD", "link": "https://aspor.canlitvme.com/aspor/aspor/playlist.m3u8", "group": "Spor"},
    {"name": "TRT Haber HD", "link": "https://trt.canlitvme.com/trthaber/trthaber/playlist.m3u8", "group": "Haber"},
    {"name": "NTV HD", "link": "https://ntv.canlitvme.com/ntv/ntv/playlist.m3u8", "group": "Haber"},
    {"name": "CNN Türk HD", "link": "https://cnnturk.canlitvme.com/cnnturk/cnnturk/playlist.m3u8", "group": "Haber"}
]

m3u_text = "#EXTM3U\n"

for ch in channels:
    m3u_text += f'#EXTINF:-1 group-title="{ch["group"]}", {ch["name"]}\n'
    m3u_text += f"{ch['link']}\n"

with open("tv.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_text)

print("tv.m3u faylı birbaşa və bloklanmayan rəsmi linklərlə yeniləndi!")
