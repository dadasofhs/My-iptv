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

channels = [
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
    {"name": "ATV HD", "url": "https://www.atv.com.tr/canli-yayin", "backup": "https://atv.canlitvme.com/atv/atv/playlist.m3u8", "group": "Ulusal"},
    {"name": "Kanal D HD", "url": "https://www.kanald.com.tr/canli-yayin", "backup": "https://kanald.canlitvme.com/kanald/kanald/playlist.m3u8", "group": "Ulusal"},
    {"name": "Star TV HD", "url": "https://www.startv.com.tr/canli-yayin", "backup": "https://star.canlitvme.com/star/star/playlist.m3u8", "group": "Ulusal"},
    {"name": "Show TV HD", "url": "https://www.showtv.com.tr/canli-yayin", "backup": "https://show.canlitvme.com/show/show/playlist.m3u8", "group": "Ulusal"},
    {"name": "TV8 HD", "url": "https://www.tv8.com.tr/canli-yayin", "backup": "https://tv8.canlitvme.com/tv8/tv8/playlist.m3u8", "group": "Ulusal"},
    {"name": "TRT 1 HD", "url": "https://www.trtizle.com/canli/tv/trt-1", "backup": "https://trt.canlitvme.com/trt1/trt1/playlist.m3u8", "group": "Ulusal"},
    {"name": "NOW TV HD", "url": "https://www.nowtv.com.tr/canli-yayin", "backup": "https://fox.canlitvme.com/fox/fox/playlist.m3u8", "group": "Ulusal"},
    {"name": "Kanal 7 HD", "url": "https://www.kanal7.com/canli-izle", "backup": "https://kanal7.canlitvme.com/kanal7/kanal7/playlist.m3u8", "group": "Ulusal"},
    {"name": "Beyaz TV HD", "url": "https://beyaztv.com.tr/canli-yayin", "backup": "https://beyaz.canlitvme.com/beyaz/beyaz/playlist.m3u8", "group": "Ulusal"},
    {"name": "A2 TV HD", "url": "https://www.atv.com.tr/a2tv/canli-yayin", "backup": "https://a2.canlitvme.com/a2/a2/playlist.m3u8", "group": "Ulusal"},
    {"name": "TRT Spor HD", "url": "https://www.trtizle.com/canli/tv/trt-spor", "backup": "https://trt.canlitvme.com/trtspor/trtspor/playlist.m3u8", "group": "Spor"},
    {"name": "A Spor HD", "url": "https://www.aspor.com.tr/canli-yayin", "backup": "https://aspor.canlitvme.com/aspor/aspor/playlist.m3u8", "group": "Spor"},
    {"name": "Sports TV HD", "url": "https://www.sportstv.com.tr/canli", "backup": "https://sportstv.canlitvme.com/sportstv/sportstv/playlist.m3u8", "group": "Spor"},
    {"name": "TRT Haber HD", "url": "https://www.trtizle.com/canli/tv/trt-haber", "backup": "https://trt.canlitvme.com/trthaber/trthaber/playlist.m3u8", "group": "Haber"},
    {"name": "A Haber HD", "url": "https://www.ahaber.com.tr/canli-yayin", "backup": "https://ahaber.canlitvme.com/ahaber/ahaber/playlist.m3u8", "group": "Haber"},
    {"name": "NTV HD", "url": "https://www.ntv.com.tr/canli-yayin", "backup": "https://ntv.canlitvme.com/ntv/ntv/playlist.m3u8", "group": "Haber"},
    {"name": "CNN Türk HD", "url": "https://www.cnnturk.com/canli-yayin", "backup": "https://cnnturk.canlitvme.com/cnnturk/cnnturk/playlist.m3u8", "group": "Haber"},
    {"name": "HaberTürk HD", "url": "https://www.haberturk.com/canli-yayin", "backup": "https://haberturk.canlitvme.com/haberturk/haberturk/playlist.m3u8", "group": "Haber"},
    {"name": "Sözcü TV HD", "url": "https://www.szctv.com.tr/canli-yayin", "backup": "https://sozcu.canlitvme.com/sozcu/sozcu/playlist.m3u8", "group": "Haber"},
    {"name": "Halk TV HD", "url": "https://halktv.com.tr/canli-yayin", "backup": "https://halktv.canlitvme.com/halktv/halktv/playlist.m3u8", "group": "Haber"}
]

m3u_text = "#EXTM3U\n"

for ch in channels:
    print(f"{ch['name']} linki axtarılır...")
    live_link = get_channel_link(ch["url"], ch["backup"])
    m3u_text += f'#EXTINF:-1 group-title="{ch["group"]}", {ch["name"]}\n'
    m3u_text += f"{live_link}\n"

with open("tv.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_text)

print("\nUğurlu! tv.m3u faylı xətasız şəkildə tam yeniləndi!")
