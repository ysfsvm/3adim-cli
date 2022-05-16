#!/usr/bin/env python3
import requests
from urllib.parse import urlparse

dersliste_url = 'https://ogmmateryal.eba.gov.tr/api/uc-adim-ders-listele/TYT' 
konuliste_url = 'https://ogmmateryal.eba.gov.tr/api/uc-adim-konu-listele/1234-ayt' 
soruliste_url = 'https://ogmmateryal.eba.gov.tr/api/uc-adim-soru-listele?kategori=TYT,AYT,YDT&konu=56&adim=1'
soru_url = "https://ogmmateryal.eba.gov.tr/panel/upload/ucadim/aaa.mp4"
dersliste = urlparse(dersliste_url)
konuliste = urlparse(konuliste_url)
soruliste = urlparse(soruliste_url)
soru = urlparse(soru_url)

sinav_secimi = int(input("Sınav Seçin:\n1.TYT\n2.AYT\n3.YDT\nSeçiminiz: "))
if sinav_secimi == 1:
    sinav_secimi = "TYT"
elif sinav_secimi == 2:
    sinav_secimi = "AYT"
elif sinav_secimi == 3:
    sinav_secimi = "YDT"
else:
    print("Lütfen Doğru Bir değer girin!")
    quit()

sinav_link = dersliste._replace(path="/api/uc-adim-ders-listele/" + sinav_secimi).geturl()
sinav_json = requests.get(sinav_link).json()

for i in range(len(sinav_json)):
        ders_baslik = sinav_json[i]["baslik"]
        ders_id = sinav_json[i]["id"]
        print(str(i + 1), "-", sinav_secimi ,ders_baslik)

ders_secimi = int(input("Seçiminiz: "))
if ders_secimi > len(sinav_json) or ders_secimi <= 0:
    print("Lütfen doğru bir değer girin!")
    quit()

ders = sinav_json[ders_secimi-1]["id"]
ders_baslik = sinav_json[ders_secimi-1]["baslik"]

konu_link = dersliste._replace(path="/api/uc-adim-konu-listele/" + str(ders) + "-" + sinav_secimi).geturl()
konu_json = requests.get(konu_link).json()

for i in range(len(konu_json)):
        konu_baslik = konu_json[i]["ucAdimKonu"]
        konu_id = konu_json[i]["id"]
        print(str(i + 1), "-", konu_baslik)

konu_secimi = int(input("Seçiminiz: "))
if konu_secimi > len(konu_json) or konu_secimi <= 0:
    print("Lütfen doğru bir değer girin!")
    quit()
konu = konu_json[konu_secimi-1]["id"]

adim = int(input("Kaçıncı Adım? : "))
if not  0 < adim < 4:
    print("Lütfen doğru bir değer girin!")
    quit()
soruliste_link = soruliste._replace(query="kategori=" + str(sinav_secimi) + "&" + "konu=" + str(konu) + "&" + "adim=" + str(adim)).geturl()
soruliste_json = requests.get(soruliste_link).json()

for i in range(len(soruliste_json)):
        soru_dosya = soruliste_json[i]["dosya"]
        soru_link = soru._replace(path="panel/upload/ucadim/" + soru_dosya).geturl()
        print(str(i + 1), "-", soru_link)
