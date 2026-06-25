import requests

# TV pleyerlərinin və yoxlama botunun bloklanmaması üçün başlıqlar
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "*/*"
}

# Test ediləcək əsas və alternativ Türk kanallarının siyahısı
candidate_channels = [
    # --- ULUSAL VƏ BELGESEL ---
    {"name": "TRT 1 HD", "link": "https://trt.live.enetres.net/live/trt1.m3u8", "group": "Ulusal"},
    {"name": "TRT Belgesel HD", "link": "https://trt.live.enetres.net/live/trtbelgesel.m3u8", "group": "Belgesel"},
    {"name": "Show TV HD", "link": "https://ciner-live.daioncdn.net/showtv/showtv.m3u8", "group": "Ulusal"},
    {"name": "Fox / NOW TV HD", "link": "https://now-live.daioncdn.net/now/now.m3u8", "group": "Ulusal"},
    {"name": "ATV HD", "link": "https://vvr.live.atv.com.tr/atv/atv_hd.m3u8", "group": "Ulusal"},
    {"name": "Kanal D HD", "link": "https://demiroren-live.daioncdn.net/kanald/kanald.m3u8", "group": "Ulusal"},
    {"name": "Star TV HD", "link": "https://startv.live.dygcdn.com/startv/startv.m3u8", "group": "Ulusal"},
    {"name": "TV8 HD", "link": "https://tv8-live.daioncdn.net/tv8/tv8.m3u8", "group": "Ulusal"},
    {"name": "Kanal 7 HD", "link": "https://kanal7-live.daioncdn.net/kanal7/kanal7.m3u8", "group": "Ulusal"},
    {"name": "A2 TV HD", "link": "https://vvr.live.atv.com.tr/a2/a2_hd.m3u8", "group": "Ulusal"},
    {"name": "Beyaz TV HD", "link": "https://beyaztv.live.daioncdn.net/beyaztv/beyaztv.m3u8", "group": "Ulusal"},

    # --- HABER ---
    {"name": "HaberTürk HD", "link": "https://ciner-live.daioncdn.net/haberturk/haberturk.m3u8", "group": "Haber"},
    {"name": "TRT Haber HD", "link": "https://trt.live.enetres.net/live/trthaber.m3u8", "group": "Haber"},
    {"name": "NTV HD", "link": "https://dyg-live.daioncdn.net/ntv/ntv.m3u8", "group": "Haber"},
    {"name": "CNN Türk HD", "link": "https://demiroren-live.daioncdn.net/cnnturk/cnnturk.m3u8", "group": "Haber"},
    {"name": "A Haber HD", "link": "https://turkuvaz-live.daioncdn.net/ahaber/ahaber.m3u8", "group": "Haber"},
    {"name": "Sözcü TV HD", "link": "https://szctv-live.daioncdn.net/szctv/szctv.m3u8", "group": "Haber"},
    {"name": "TGRT Haber HD", "link": "https://tgrt-live.daioncdn.net/tgrthaber/tgrthaber.m3u8", "group": "Haber"},
    {"name": "Bloomberg HT HD", "link": "https://ciner-live.daioncdn.net/bloomberght/bloomberght.m3u8", "group": "Haber"},

    # --- SPOR VƏ MÜZİK ---
    {"name": "TRT Spor HD", "link": "https://trt.live.enetres.net/live/trtspor.m3u8", "group": "Spor"},
    {"name": "A Spor HD", "link": "https://turkuvaz-live.daioncdn.net/aspor/aspor.m3u8", "group": "Spor"},
    {"name": "Fenerbahçe TV", "link": "https://fenerbahce-live.daioncdn.net/fbtv/fbtv.m3u8", "group": "Spor"},
    {"name": "TRT Müzik HD", "link": "https://trt.live.enetres.net/live/trtmuzik.m3u8", "group": "Müzik"},
    {"name": "Kral TV HD", "link": "https://dyg-live.daioncdn.net/kraltv/kraltv.m3u8", "group": "Müzik"}
]

m3u_text = "#EXTM3U\n"
valid_count = 0

print("🔍 Kanalların aktivliyi yoxlanılır...\n")

for ch in candidate_channels:
    try:
        # Linkin həqiqətən aktiv olub-olmadığını sürətli şəkildə yoxlayırıq
        response = requests.head(ch["link"], headers=headers, timeout=5, allow_redirects=True)
        
        # Əgər server uğurlu cavab verirsə, kanalı pleyistə əlavə edirik
        if response.status_code in [200, 201, 301, 302]:
            print(f"✅ AKTİV: {ch['name']}")
            m3u_text += f'#EXTINF:-1 group-title="{ch["group"]}" user-agent="Mozilla/5.0", {ch["name"]}\n'
            m3u_text += f"{ch['link']}\n"
            valid_count += 1
        else:
            print(f"❌ XƏTA ({response.status_code}): {ch['name']} siyahıya salınmadı.")
            
    except Exception as e:
        print(f"⚠️ BLOK / ÖLÜ: {ch['name']} (Xəta: {e})")

# Aktiv kanalları fayla yazırıq
with open("tv.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_text)

print(f"\n✨ Skan tamamlandı! {valid_count} ədəd tam işlək kanal tv.m3u faylına yazıldı.")

