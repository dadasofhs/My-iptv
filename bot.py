import requests  # Saytlara sorğu göndərmək və ordakı məlumatları (HTML kodunu) yükləmək üçün kitabxana
import re        # Mətnlərin içindən xüsusi qaydalarla (məsələn, .m3u8 ilə bitən linkləri) axtarıb tapmaq üçün (Regular Expressions) kitabxanası

# 1. HƏDƏF VƏ TƏHLÜKƏSİZLİK AYARLARI
# DMAX kanalının canlı yayımının yerləşdiyi saytın tam linki
url = "https://www.canlitvme.com/dmax-canli-izle-1"

# "User-Agent" sayta bizim bir proqram deyil, normal bir kompüter brauzeri (məsələn, Google Chrome) olduğumuzu demək üçün lazımdır.
# Əgər bunu yazmasaq, sayt bizi "bot" hesab edib bloklayar.
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

# 2. SAYTDAN CANLI YAYIM LİNKİNİN AXTARILMASI (TRY-EXCEPT BLOKU)
# Burada proqramı "yoxlama rejimində" işlədirik. Əgər hər hansı xəta (internet kəsilməsi, saytın çökməsi və s.) olarsa, skriptimiz tamamilə dayanmasın.
try:
    # Sayta daxil oluruq və yuxarıda təyin etdiyimiz brauzer məlumatını (headers) göndəririk. 
    # timeout=10 o deməkdir ki, sayt 10 saniyə ərzində cavab verməsə, gözləməyi dayandır.
    response = requests.get(url, headers=headers, timeout=10)
    
    # re.search funksiyası saytın bütün HTML kodlarının içini gəzir.
    # r'(https://[^"\']+\.m3u8)' qaydası isə: "mənə 'https://' ilə başlayan və '.m3u8' ilə bitən linki tap gətir" deməkdir.
    match = re.search(r'(https://[^"\']+\.m3u8)', response.text)
    
    # Əgər saytın içində belə bir link TAPILSA:
    if match:
        stream_link = match.group(1)  # Tapılan həmin aktiv linki (məsələn, cdn linkini) "stream_link" dəyişəninə mənimsət.
        print("Uğurlu: Saytdan yeni canlı yayım linki tapıldı:", stream_link)
        
    # Əgər sayt kodu dəyişibsə və `.m3u8` linki tapılmırsa (bayaq səndə olan problem):
    else:
        # Skript dayanmır, ehtiyat olaraq sənin Web Video Caster-dən tapdığın o işlək sabit linki götürür.
        stream_link = "https://cdn508.canlitvme.com/dmax/dmax/playlist.m3u8"
        print("Xəbərdarlıq: Saytdan link tapılmadı, ehtiyat (backup) link işə salındı.")
        
# Əgər internet tamamilə qopsa və ya sayta heç müraciət etmək mümkün olmasa (Xəta baş versə):
except Exception as e:
    # Yenə də skript çökmür, birbaşa ehtiyat linki təyin edir ki, IPTV pleyerin boş qalmasın.
    stream_link = "https://cdn508.canlitvme.com/dmax/dmax/playlist.m3u8"
    print("Sistem Xətası baş verdi, ehtiyat link bərpa olundu. Xəta mesajı:", e)

# 3. TELEVİZORUN BLOKLANMASINI KEÇMƏK ÜÇÜN HƏLL (ƏN ÖNƏMLİ HİSSƏ)
# Bayaq televizorunda ad göründü, amma ekran qara qaldı. Çünki TV pleyeri linki birbaşa açmaq istəyəndə saytın serveri onun TV olduğunu başa düşüb yayımı kəsdi.
# İndi biz linkin sonuna şaquli xətt ( | ) qoyuruq və TV-yə əmr veririk: 
# "Bu linki açanda sayta özünü Chrome brauzeri kimi təqdim et (User-Agent) və de ki, mən bura canlitvme.com saytından yönlənib gəlmişəm (Referer)."
tv_link = f"{stream_link}|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)&Referer=https://www.canlitvme.com/"

# 4. IPTV PLEYLİST FAYLININ (tv.m3u) FORMATLANMASI
# IPTV proqramlarının (Smart TV, VLC, s.) oxuya bilməsi üçün faylı format təmizliyinə salırıq.
# \n işarəsi mətni növbəti sətrə keçirmək üçündür.
m3u_text = (
    "#EXTM3U\n"                                    # Faylın IPTV pleylisti olduğunu bildirən icbari başlıq
    '#EXTINF:-1 group-title="Belgesel",DMAX HD\n'   # Kanalın qrupunu (Sənədli film) və ekranda görünəcək adını təyin edirik
    f"{tv_link}\n"                                 # Az öncə arxasına təhlükəsizlik kodları yapışdırdığımız canlı yayım linki
)

# 5. MƏLUMATIN REPOZİTORİYAYA YAZILMASI
# "tv.m3u" adlı fayl açılır (əgər yoxdursa yaradılır, varsa içi silinib yenidən yazılır).
# encoding="utf-8" yazırıq ki, Azərbaycan/Türk hərfləri (ç, ş, ə, ı) xarab olmasın, düzgün oxunsun.
with open("tv.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_text)  # Hazırladığımız bütün mətni faylın içinə yazırıq.

print("Əməliyyat tamamlandı: tv.m3u faylı tam avtomatik və təhlükəsizlik başlıqları ilə yeniləndi!")

