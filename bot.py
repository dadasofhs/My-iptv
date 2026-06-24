import requests  
import re        

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def get_channel_link(url, backup_link):
    try:
        res = requests.get(url, headers=headers, timeout=10)
        match = re.search(r'(https://[^"\']+\.m3u8[^\s"\']*)', res.text)
        if match:
            return match.group(1)
        return backup_link
    except Exception:
        return backup_link

# 30 fərqli kanal və hər birinin özünəməxsus orijinal səhifə ünvanı
channels = [
    # --- SƏNƏDLİ FİLM (BELGESEL) KANALLARI ---
    {"name": "DMAX HD", "url": "https://tr.canlitvme.com/livetv/dmax-canli-hd/1", "backup": "https://cdn508.canlitvme.com/dmax/dmax/playlist.m3u8", "group": "Belgesel"},
    {"name": "TLC HD", "url": "https://tr.canlitvme.com/livetv/tlc-hd/1", "backup": "https://cdn508.canlitvme.com/tlc/tlc/playlist.m3u8", "group": "Belgesel"},
    {"name": "Science HD", "url": "https://tr.canlitvme.com/livetv/science-hd/1", "backup": "https://cdn508.canlitvme.com/science/science/playlist.m3u8", "group": "Belgesel"},
    {"name": "Nat Geo HD", "url": "https://tr.canlitvme.com/livetv/national-geographic-hd/1", "backup": "https://cdn508.canlitvme.com/natgeo/natgeo/playlist.m3u8", "group": "Belgesel"},
    {"name": "Nat Geo Wild HD", "url": "https://tr.canlitvme.com/livetv/nat-geo-wild-hd/1", "backup": "https://cdn508.canlitvme.com/natgeowild/natgeowild/playlist.m3u8", "group": "Belgesel"},
    {"name": "History Channel HD", "url": "https://tr.canlitvme.com/livetv/history-channel-hd/1", "backup": "https://cdn508.canlitvme.com/history/history/playlist.m3u8", "group": "Belgesel"},
    {"name": "TRT Belgesel HD", "url": "https://www.trtizle.com/canli/tv/trt-belgesel", "backup": "https://trt.canlitvme.com/trtbelgesel/trtbelgesel/playlist.m3u8", "group": "Belgesel"},
    {"name": "BBC Earth HD", "url": "https://tr.canlitvme.com/livetv/bbc-earth-hd/1", "backup": "https://cdn508.canlitvme.com/bbcearth/bbcearth/playlist.m3u8", "group": "Belgesel"},
    {"name": "Discovery Channel HD", "url": "https://tr.canlitvme.com/livetv/discovery-channel-hd/1", "backup": "https://cdn508.canlitvme.com/discovery/discovery/playlist.m3u8", "group": "Belgesel"},
    {"name": "ID Xtra HD", "url": "https://tr.canlitvme.com/livetv/investigation-discovery-id-hd/1", "backup": "https://cdn508.canlitvme.com/idx/idx/playlist.m3u8", "group": "Belgesel"},

    # --- ÜMUMİ VƏ POPULYAR KANALLAR ---
    {"name": "ATV HD", "url": "https://www.atv.com.tr/canli-yayin", "backup": "https://atv.canlitvme.com/atv/atv/playlist.m3u8", "group": "Ulusal"},
    {"name": "Kanal D HD", "url": "https://www.kanald.com.tr/canli-yayin", "backup": "https://kanald.canlitvme.com/kanald/kanald/playlist.m3u8", "group": "Ulusal"},

