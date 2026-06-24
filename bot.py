import requests
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://tr.canlitvme.com/",
    "Origin": "https://tr.canlitvme.com"
}

def get_link():
    try:
        res = requests.get("https://tr.canlitvme.com/dmax-canli-hd", headers=HEADERS, timeout=15)
        if res.status_code == 200:
            # Həm normal .m3u8, həm də parametrləri olan (?...) linkləri tapmaq üçün reqex yeniləndi
            match = re.search(r'(https?://[^\s"\']+\.m3u8(?:[^\s"\']*)?)', res.text)
            if match:
                clean_link = match.group(1).replace("&amp;", "&")
                return clean_link
    except Exception as e:
        print(f"Xəta baş verdi: {e}")
    return None

link = get_link()

if link:
    m3u_text = f'#EXTM3U\n#EXTINF:-1 group-title="Belgesel",DMAX HD\n{link}\n'
    with open("tv.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_text)
    print("Yeniləndi! Tapılan link:", link)
else:
    # GitHub Actions xəta verməsin deyə boş da olsa fayl yaradırıq
    with open("tv.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n#EXTINF:-1 group-title=\"Belgesel\",DMAX HD\n# Link bu dəfə tapılmadı\n")
    print("Link tapılmadı, amma boş tv.m3u faylı yaradıldı.")
    
