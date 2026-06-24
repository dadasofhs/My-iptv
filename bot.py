import requests
import re

# Canlı TV saytından DMAX-ın səhifəsini oxuyuruq
url = "https://www.canlitvme.com/dmax-canli-izle-1"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

try:
    response = requests.get(url, headers=headers, timeout=10)
    # Səhifənin kodları arasından avtomatik .m3u8 linkini axtarırıq
    match = re.search(r'(https://[^"\']+\.m3u8)', response.text)
    
    if match:
        stream_link = match.group(1)
        print("Yeni link tapıldı:", stream_link)
    else:
        # Əgər tapılmasa, sonuncu bildiyimiz işlək linki ehtiyat kimi qoyuruq
        stream_link = "https://cdn508.canlitvme.com/dmax/dmax/playlist.m3u8"
        print("Saytdan link tapılmadı, ehtiyat link qoyuldu.")
        
except Exception as e:
    stream_link = "https://cdn508.canlitvme.com/dmax/dmax/playlist.m3u8"
    print("Xəta baş verdi, ehtiyat link qoyuldu:", e)

# IPTV faylını hazırlayırıq
m3u_text = f'#EXTM3U\n#EXTINF:-1 group-title="Belgesel",DMAX HD\n{stream_link}\n'

with open("tv.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_text)

print("tv.m3u faylı uğurla yeniləndi!")

