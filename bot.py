import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "*/*"
}

# NƏ QƏDƏR POPULYAR TÜRK KANALI VARSA - TAM SİYAHI
candidate_channels = [
    # --- GENEL / ULUSAL KANALLAR ---
    {"name": "TRT 1 HD", "link": "https://trt.live.enetres.net/live/trt1.m3u8", "group": "Ulusal"},
    {"name": "ATV HD", "link": "https://vvr.live.atv.com.tr/atv/atv_hd.m3u8", "group": "Ulusal"},
    {"name": "Kanal D HD", "link": "https://demiroren-live.daioncdn.net/kanald/kanald.m3u8", "group": "Ulusal"},
    {"name": "Star TV HD", "link": "https://startv.live.dygcdn.com/startv/startv.m3u8", "group": "Ulusal"},
    {"name": "Show TV HD", "link": "https://ciner-live.daioncdn.net/showtv/showtv.m3u8", "group": "Ulusal"},
    {"name": "TV8 HD", "link": "https://tv8-live.daioncdn.net/tv8/tv8.m3u8", "group": "Ulusal"},
    {"name": "NOW TV HD", "link": "https://now-live.daioncdn.net/now/now.m3u8", "group": "Ulusal"},
    {"name": "Kanal 7 HD", "link": "https://kanal7-live.daioncdn.net/kanal7/kanal7.m3u8", "group": "Ulusal"},
    {"name": "A2 TV HD", "link": "https://vvr.live.atv.com.tr/a2/a2_hd.m3u8", "group": "Ulusal"},
    {"name": "Beyaz TV HD", "link": "https://beyaztv.live.daioncdn.net/beyaztv/beyaztv.m3u8", "group": "Ulusal"},
    {"name": "Ülke TV HD", "link": "https://ulketv-live.daioncdn.net/ulketv/ulketv.m3u8", "group": "Ulusal"},
    {"name": "TRT Türk HD", "link": "https://trt.live.enetres.net/live/trtturk.m3u8", "group": "Ulusal"},
    {"name": "TV8.5 HD", "link": "https://tv8-5-live.daioncdn.net/tv8-5/tv8-5.m3u8", "group": "Ulusal"},
    {"name": "Teve2 HD", "link": "https://demiroren-live.daioncdn.net/teve2/teve2.m3u8", "group": "Ulusal"},
    {"name": "TLC HD (Yedek)", "link": "https://cdn508.canlitvme.com/tlc/tlc/playlist.m3u8", "group": "Ulusal"},
    {"name": "DMAX HD (Yedek)", "link": "https://cdn508.canlitvme.com/dmax/dmax/playlist.m3u8", "group": "Ulusal"},
    {"name": "360 TV HD", "link": "https://turkmedya-live.daioncdn.net/tv360/tv360.m3u8", "group": "Ulusal"},

    # --- SƏNƏDLİ FİLM (BELGESEL) ---
    {"name": "TRT Belgesel HD", "link": "https://trt.live.enetres.net/live/trtbelgesel.m3u8", "group": "Belgesel"},

    # --- XƏBƏR KANALLARI (HABER) ---
    {"name": "HaberTürk HD", "link": "https://ciner-live.daioncdn.net/haberturk/haberturk.m3u8", "group": "Haber"},
    {"name": "TRT Haber HD", "link": "https://trt.live.enetres.net/live/trthaber.m3u8", "group": "Haber"},
    {"name": "NTV HD", "link": "https://dyg-live.daioncdn.net/ntv/ntv.m3u8", "group": "Haber"},
    {"name": "CNN Türk HD", "link": "https://demiroren-live.daioncdn.net/cnnturk/cnnturk.m3u8", "group": "Haber"},
    {"name": "A Haber HD", "link": "https://turkuvaz-live.daioncdn.net/ahaber/ahaber.m3u8", "group": "Haber"},
    {"name": "Sözcü TV HD", "link": "https://szctv-live.daioncdn.net/szctv/szctv.m3u8", "group": "Haber"},
    {"name": "TGRT Haber HD", "link": "https://tgrt-live.daioncdn.net/tgrthaber/tgrthaber.m3u8", "group": "Haber"},
    {"name": "Bloomberg HT HD", "link": "https://ciner-live.daioncdn.net/bloomberght/bloomberght.m3u8", "group": "Haber"},
    {"name": "Halk TV HD", "link": "https://halktv.live.daioncdn.net/halktv/halktv.m3u8", "group": "Haber"},
    {"name": "24 TV HD", "link": "https://turkmedya-live.daioncdn.net/tv24/tv24.m3u8", "group": "Haber"},
    {"name": "Ekol TV HD", "link": "https://ekoltv.live.daioncdn.net/ekoltv/ekoltv.m3u8", "group": "Haber"},
    {"name": "Kontv HD", "link": "https://kontv.live.daioncdn.net/kontv/kontv.m3u8", "group": "Haber"},
    {"name": "Kanal B HD", "link": "https://kanalb.live.daioncdn.net/kanalb/kanalb.m3u8", "group": "Haber"},

    # --- İDMAN (SPOR) ---
    {"name": "TRT Spor HD", "link": "https://trt.live.enetres.net/live/trtspor.m3u8", "group": "Spor"},
    {"name": "TRT Spor Yıldız", "link": "https://trt.live.enetres.net/live/trtsporyildiz.m3u8", "group": "Spor"},
    {"name": "A Spor HD", "link": "https://turkuvaz-live.daioncdn.net/aspor/aspor.m3u8", "group": "Spor"},
    {"name": "Fenerbahçe TV", "link": "https://fenerbahce-live.daioncdn.net/fbtv/fbtv.m3u8", "group": "Spor"},
    {"name": "Sports TV HD", "link": "https://sportstv.canlitvme.com/sportstv/sportstv/playlist.m3u8", "group": "Spor"},

    # --- MUSİQİ (MÜZİK) ---
    {"name": "TRT Müzik HD", "link": "https://trt.live.enetres.net/live/trtmuzik.m3u8", "group": "Müzik"},
    {"name": "Kral TV HD", "link": "https://dyg-live.daioncdn.net/kraltv/kraltv.m3u8", "group": "Müzik"},
    {"name": "Dream Türk HD", "link": "https://demiroren-live.daioncdn.net/dreamturk/dreamturk.m3u8", "group": "Müzik"},
    {"name": "Number One Türk HD", "link": "https://numberone.live.daioncdn.net/n1turk/n1turk.m3u8", "group": "Müzik"},

    # --- UŞAQ (ÇOCUK) ---
    {"name": "TRT Çocuk HD", "link": "https://trt.live.enetres.net/live/trtcocuk.m3u8", "group": "Çocuk"},
    {"name": "Minika GO HD", "link": "https://turkuvaz-live.daioncdn.net/minikago/minikago.m3u8", "group": "Çocuk"},
    {"name": "Minika Çocuk HD", "link": "https://turkuvaz-live.daioncdn.net/minikacocuk/minikacocuk.m3u8", "group": "Çocuk"}
]

m3u_text = "#EXTM3U\n"
valid_count = 0

print("🔍 Bütün Türk kanalları süzgəcdən keçirilir...\n")

for ch in candidate_channels:
    try:
        # Sürətli cavab yoxlaması
        response = requests.head(ch["link"], headers=headers, timeout=4, allow_redirects=True)
        
        if response.status_code in [200, 201, 301, 302]:
            print(f"✅ İŞLƏYİR: {ch['name']}")
            m3u_text += f'#EXTINF:-1 group-title="{ch["group"]}" user-agent="Mozilla/5.0", {ch["name"]}\n'
            m3u_text += f"{ch['link']}\n"
            valid_count += 1
        else:
            print(f"❌ XƏTA (Kod {response.status_code}): {ch['name']}")
            
    except Exception:
        print(f"⚠️ BLOKLANIB / DIŞ IP-YƏ QAPALI: {ch['name']}")

with open("tv.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_text)

print(f"\n✨ Proses bitdi! {valid_count} ədəd tam işlək Türk kanalı fayla yazıldı.")

