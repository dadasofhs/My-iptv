import requests  
import re        

url = "https://www.canlitvme.com/dmax-canli-izle-1"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

try:
    response = requests.get(url, headers=headers, timeout=10)
    match = re.search(r'(https://[^"\']+\.m3u8)', response.text)
    
    if match:
        stream_link = match.group(1)
        print("Saytdan link tapıldı:", stream_link)
    else:
        stream_link = "https://cdn508.canlitvme.com/dmax/dmax/playlist.m3u8"
        print("Ehtiyat link işə salındı.")
        
except Exception as e:
    stream_link = "https://cdn508.canlitvme.com/dmax/dmax/playlist.m3u8"
    print("Xəta baş verdi, ehtiyat link qoyuldu:", e)

# ─── YENİ HƏLL HİSSƏSİ ───
# Çarəsiz qaldıqda, linki açıq proxy server vasitəsilə yönləndiririk.
# Bu proxy avtomatik olaraq bütün lazımi brauzer başlıqlarını arxa fonda həll edir.
proxy_url = f"https://worker-curly-glitter-4293.workers.dev/?url={stream_link}"

m3u_text = (
    "#EXTM3U\n"
    '#EXTINF:-1 group-title="Belgesel",DMAX HD\n'
    f"{proxy_url}\n"
)

with open("tv.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_text)

print("tv.m3u faylı Proxy linki ilə uğurla yeniləndi!")


