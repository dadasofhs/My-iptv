# Tamamilə rəsmi və qorumasız türk kanallarının yayım siyahısı
channels = [
    # --- BELGESEL (SƏNƏDLİ FİLM) ---
    {"name": "TRT Belgesel HD", "link": "https://trt.live.enetres.net/live/trtbelgesel.m3u8", "group": "Belgesel"},
    
    # --- ULUSAL (ÜMUMİ KANALLAR) ---
    {"name": "TRT 1 HD", "link": "https://trt.live.enetres.net/live/trt1.m3u8", "group": "Ulusal"},
    {"name": "Show TV HD", "link": "https://ciner-live.daioncdn.net/showtv/showtv.m3u8", "group": "Ulusal"},
    {"name": "Fox / NOW TV HD", "link": "https://now-live.daioncdn.net/now/now.m3u8", "group": "Ulusal"},
    {"name": "Kanal 7 HD", "link": "https://kanal7-live.daioncdn.net/kanal7/kanal7.m3u8", "group": "Ulusal"},
    {"name": "Ülke TV HD", "link": "https://ulketv-live.daioncdn.net/ulketv/ulketv.m3u8", "group": "Ulusal"},
    {"name": "TRT Türk HD", "link": "https://trt.live.enetres.net/live/trtturk.m3u8", "group": "Ulusal"},
    
    # --- HABER (XƏBƏR) ---
    {"name": "HaberTürk HD", "link": "https://ciner-live.daioncdn.net/haberturk/haberturk.m3u8", "group": "Haber"},
    {"name": "TRT Haber HD", "link": "https://trt.live.enetres.net/live/trthaber.m3u8", "group": "Haber"},
    {"name": "NTV HD", "link": "https://dyg-live.daioncdn.net/ntv/ntv.m3u8", "group": "Haber"},
    {"name": "CNN Türk HD", "link": "https://demiroren-live.daioncdn.net/cnnturk/cnnturk.m3u8", "group": "Haber"},
    {"name": "A Haber HD", "link": "https://turkuvaz-live.daioncdn.net/ahaber/ahaber.m3u8", "group": "Haber"},
    {"name": "TGRT Haber HD", "link": "https://tgrt-live.daioncdn.net/tgrthaber/tgrthaber.m3u8", "group": "Haber"},
    {"name": "Bloomberg HT HD", "link": "https://ciner-live.daioncdn.net/bloomberght/bloomberght.m3u8", "group": "Haber"},
    
    # --- SPOR (İDMAN) ---
    {"name": "TRT Spor HD", "link": "https://trt.live.enetres.net/live/trtspor.m3u8", "group": "Spor"},
    {"name": "TRT Spor Yıldız", "link": "https://trt.live.enetres.net/live/trtsporyildiz.m3u8", "group": "Spor"},
    {"name": "A Spor HD", "link": "https://turkuvaz-live.daioncdn.net/aspor/aspor.m3u8", "group": "Spor"},
    {"name": "Fenerbahçe TV (FB TV)", "link": "https://fenerbahce-live.daioncdn.net/fbtv/fbtv.m3u8", "group": "Spor"},
    
    # --- MÜZİK VƏ ÇOCUK ---
    {"name": "TRT Müzik HD", "link": "https://trt.live.enetres.net/live/trtmuzik.m3u8", "group": "Müzik"},
    {"name": "Kral TV HD", "link": "https://dyg-live.daioncdn.net/kraltv/kraltv.m3u8", "group": "Müzik"},
    {"name": "TRT Çocuk HD", "link": "https://trt.live.enetres.net/live/trtcocuk.m3u8", "group": "Çocuk"}
]

m3u_text = "#EXTM3U\n"

for ch in channels:
    # Pleyer xətalarının qarşısını almaq üçün user-agent teqi əlavə edirik
    m3u_text += f'#EXTINF:-1 group-title="{ch["group"]}" user-agent="Mozilla/5.0", {ch["name"]}\n'
    m3u_text += f"{ch['link']}\n"

with open("tv.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_text)

print("tv.m3u faylı rəsmi türk kanalları paketi ilə yeniləndi!")
