link = "https://cdn508.canlitvme.com/dmax/dmax/playlist.m3u8"

m3u_text = f'#EXTM3U\n#EXTINF:-1 group-title="Belgesel",DMAX HD\n{link}\n'
with open("tv.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_text)
print("Yeniləndi!")


