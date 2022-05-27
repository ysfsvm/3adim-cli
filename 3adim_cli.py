#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : github/ysfsvm
# Created Date: 15/05/2022
# version = 0.9.1
# license = GNU GPL v3
#----------------------------------------------------------------------------

import os
import time
import requests
from pathlib import Path
from urllib.parse import urlparse
import urllib.request

baseUrl = 'https://ogmmateryal.eba.gov.tr/' 
soruliste_url = 'https://ogmmateryal.eba.gov.tr/api/uc-adim-soru-listele'
base = urlparse(baseUrl)
soruliste = urlparse(soruliste_url)

# Bruh wincort
if os.name == 'nt':
    cortmode = 1
    folders = "\\"
else:
    cortmode = 0
    folders = "/"

def downloadfile(url, name):
    urllib.request.urlretrieve(url, name)

def downloadQuestions():
        global dirname
        if cortmode: dirname = os.environ['USERPROFILE'] + "\\Videos\\" + str(konuAdi) + " - " + str(adim) + ".adım Soruları"
        else: dirname = str(os.getcwd()) + "/" + str(konuAdi) + " - " + str(adim) + ".adım Soruları"

        Path(dirname).mkdir(parents=True, exist_ok=True)
        downloadfile(soru_link , dirname + "/" + "soru-" + str(i + 1) + ".mp4")
        print("soru-" + str(i + 1) + ".mp4" + " başarı ile indirildi!")

def downloadFullQuestions():
        global dirname
        if cortmode: dirname = os.environ['USERPROFILE'] + "\\Videos\\" + str(konuAdi) + " - " + str(fullAdim) + ".adım Soruları"
        else: dirname = str(os.getcwd()) + "/" + str(konuAdi) + " - " + str(fullAdim) + ".adım Soruları"

        Path(dirname).mkdir(parents=True, exist_ok=True)
        downloadfile(soruFull_link , dirname + "/" + "soru-" + str(i + 1) + ".mp4")
        print(str(fullAdim) + ".Adım - soru-" + str(i + 1) + ".mp4" + " başarı ile indirildi!")

def wrongAnswer():
    print("Lütfen doğru bir değer girin!")
    quit()

def fetchLink(path, answer):
    link= base._replace(path=path + answer).geturl()
    baselink = requests.get(link)
    linkJson = baselink.json()
    return linkJson

def askDownload():
    quest = input("Dosyaları indirmek istiyor musunuz? [evet (Adımı indir) / hayır (Adımın soru linkleri) / full (tüm konu) ]: ")
    if quest == "evet":
        return 1
    if quest == "hayır":
        return 0
    if quest == "full":
        return 3
    else:
        wrongAnswer()

sinav_secimi = int(input("Sınav Seçin:\n1.TYT\n2.AYT\n3.YDT\nSeçiminiz: "))
if sinav_secimi == 1:
    sinav_secimi = "TYT"
elif sinav_secimi == 2:
    sinav_secimi = "AYT"
elif sinav_secimi == 3:
    sinav_secimi = "YDT"
else: wrongAnswer()

sinavJson = fetchLink("/api/uc-adim-ders-listele/", sinav_secimi)

for i in range(len(sinavJson)):
        ders_baslik = sinavJson[i]["baslik"]
        ders_id = sinavJson[i]["id"]
        print(str(i + 1), "-", sinav_secimi ,ders_baslik)

ders_secimi = int(input("Seçiminiz: "))
if ders_secimi > len(sinavJson) or ders_secimi <= 0: wrongAnswer()

ders = sinavJson[ders_secimi-1]["id"]
ders_baslik = sinavJson[ders_secimi-1]["baslik"]

konuJson = fetchLink("/api/uc-adim-konu-listele/" + str(ders) + "-", sinav_secimi)

for i in range(len(konuJson)):
        konu_baslik = konuJson[i]["ucAdimKonu"]
        konu_id = konuJson[i]["id"]
        print(str(i + 1), "-", konu_baslik)

konu_secimi = int(input("Seçiminiz: "))
if konu_secimi > len(konuJson) or konu_secimi <= 0: wrongAnswer()
konu = konuJson[konu_secimi-1]["id"]
konuAdi = konuJson[konu_secimi-1]["ucAdimKonu"]

down = askDownload()

if down == 1 or down == 0:
    adim = int(input("Kaçıncı Adım? : "))
    if not  0 < adim < 4: wrongAnswer()

if down == 1 or down == 0:
    soruliste_link = soruliste._replace(query="kategori=" + str(sinav_secimi) + "&" + "konu=" + str(konu) + "&" + "adim=" + str(adim)).geturl()
    soruliste_json = requests.get(soruliste_link).json()
    for i in range(len(soruliste_json)):
            soru_dosya = soruliste_json[i]["dosya"]
            soru_link = base._replace(path="panel/upload/ucadim/" + soru_dosya).geturl()
            if down == 1 : downloadQuestions()
            else: print(str(i + 1) + ".soru - " + soru_link)
    if down == 1: print("\nTest klasörünün konumu: " + dirname )

if down == 3:
    for fullAdim in range(1,4):
        sorulisteFull_link = soruliste._replace(query="kategori=" + str(sinav_secimi) + "&" + "konu=" + str(konu) + "&" + "adim=" + str(fullAdim)).geturl()
        sorulisteFull_json = requests.get(sorulisteFull_link).json()
        for i in range(len(sorulisteFull_json)):
            soruFull_dosya = sorulisteFull_json[i]["dosya"]
            soruFull_link = base._replace(path="panel/upload/ucadim/" + soruFull_dosya).geturl()
            downloadFullQuestions()
        print("\nTest klasörünün konumu: " + dirname + "\n")

print("\nÇıkmak için CTRL + C")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
