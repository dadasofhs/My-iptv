import requests  
import re        

# Bütün sorğular üçün istifadə olunacaq ortaq brauzer başlıqları
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://tr.canlitvme.com/",
    "Origin": "https://tr.canlitvme.com"
}

# Linkləri təhlükəsiz şəkildə tapmaq üçün köməkçi funksiya
def get_channel_link(url, backup_link):
    try:
        res = requests.get(url, headers=headers, timeout=10)
        match = re.search(r'(https://[^"\']+\.m3u8[^\s"\']*)', res.text)
        return match.group(1) if match else backup_link
    except Exception:
        return backup_link

# 1. DMAX HD
dmax_link = get_channel_link(
    "https://tr.canlitvme.com/livetv/dmax-canli-hd/1", 
    "https://cdn508.canlitvme.com/dmax/dmax/playlist.m3u8"
)

# 2. TLC HD
tlc_link = get_channel_link(
    "https://tr.canlitvme.com/livetv/tlc-hd/1", 
    "https://cdn508.canlitvme.com/tlc/tlc/playlist.m3u8"
)

# 3. SCIENCE HD (Bilim)
science_link = get_channel_link(
    "https://tr.canlitvme.com/livetv/science-hd/1", 
    "https://cdn508.canlitvme.com/science/science/playlist.m3u8"
)

# 4. NAT GEO HD (National Geographic)
natgeo_link = get_channel_link(
    "https://tr.canlitvme.com/livetv/national-geographic-hd/1", 
    "https://cdn508.canlitvme.com/natgeo/natgeo/playlist.m3u8"
)

# IPTV PLEYLİST FAYLININ FORMATLANMASI (4 KANAL ARDICIL)
m3u_text = (
    "#EXTM3U\n"
    '#EXTINF:-1 group-title="Belgesel",DMAX HD\n'
    f"{dmax_link}\n"
    '#EXTINF:-1 group-title="Belgesel",TLC HD\n'
    f"{tlc_link}\n"
    '#EXTINF:-1 group-title="Belgesel",Science HD\n'
    f"{science_link}\n"
    '#EXTINF:-1 group-title="Belgesel",Nat Geo HD\n'
    f"{natgeo_link}\n"
)

with open("tv.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_text)

print("tv.m3u faylı uğurla yeniləndi: Siyahıda artıq 4 sənədli film kanalı var!")

