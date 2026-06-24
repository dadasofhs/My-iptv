import requests  
import re        

url = "https://www.canlitvme.com/dmax-canli-izle-1"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

try:
    response = requests.get(url, headers=headers, timeout=10)
    match = re.search(r'(https://[^"\']+\.m3u8)', response.text)
    
    if match:
        stream_link = match.group(1)
        print("Saytdan yeni link tapıldı:", stream_link)
    else:
        stream_link = "https://cdn508.canlitvme.com/dmax/dmax/playlist.m3u8"
        print("Ehtiyat link işə salındı.")
        
except Exception as e:
    stream_link = "https://cdn508.canlitvme.com/dmax/dmax/playlist.m3u8"
    print("Xəta baş verdi, ehtiyat link qoyuldu:", e)

# BU HİSSƏ DƏYİŞDİ: İndi hər iki IPTV standartını eyni anda yazırıq.
# Həm pleyerin daxili oxuyucusu üçün #EXTVLCOPT parametrlərini, 
# həm də bəzi pleyerlərin sevdiyi şaquli xətt (|) üsulunu birlikdə veririk.
m3u_text = (
    "#EXTM3U\n"
    '#EXTINF:-1 group-title="Belgesel",DMAX HD\n'
    f'#EXTVLCOPT:http-user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"\n'
    f'#EXTVLCOPT:http-referrer="https://www.canlitvme.com/"\n'
    f'{stream_link}|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)&Referer=https://www.canlitvme.com/\n'
)

with open("tv.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_text)

print("tv.m3u faylı tam zəmanətli formatda yeniləndi!")

