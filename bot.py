import requests  
import re        

# Sənin göndərdiyin tam və dəqiq link:
url = "https://tr.canlitvme.com/livetv/dmax-canli-hd/1"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

try:
    response = requests.get(url, headers=headers, timeout=10)
    # Səhifə daxilindən yayım linkini tapırıq
    match = re.search(r'(https://[^"\']+\.m3u8)', response.text)
    
    if match:
        stream_link = match.group(1)
        print("Dəqiq linkdən canlı yayım tapıldı:", stream_link)
    else:
        stream_link = "https://cdn508.canlitvme.com/dmax/dmax/playlist.m3u8"
        print("Link tapılmadı, ehtiyat işə salındı.")
        
except Exception as e:
    stream_link = "https://cdn508.canlitvme.com/dmax/dmax/playlist.m3u8"
    print("Xəta baş verdi:", e)

# TV-nin bloklanmasını kökündən həll edən yönləndirici (Proxy) linkimiz:
proxy_url = f"https://worker-curly-glitter-4293.workers.dev/?url={stream_link}"

m3u_text = (
    "#EXTM3U\n"
    '#EXTINF:-1 group-title="Belgesel",DMAX HD\n'
    f"{proxy_url}\n"
)

with open("tv.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_text)

print("tv.m3u faylı yeni hədəf linklə uğurla yeniləndi!")

