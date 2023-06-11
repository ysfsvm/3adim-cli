import os
import time
import requests
from urllib.parse import urlparse
import urllib.request
import re
import json
import locale
import platform

baseUrl = 'https://ogmmateryal.eba.gov.tr/' 
soruliste_url = 'https://ogmmateryal.eba.gov.tr/api/uc-adim-soru-listele'
base = urlparse(baseUrl)
soruliste = urlparse(soruliste_url)

system_language = locale.getlocale()[0]
if system_language.startswith("Turk"):
    system_language = "tr"
elif system_language.startswith("Eng"):
    system_language = "en"
else:
    system_language = "en"

lang_file_path = f"lang/output-{system_language}.json"
if not os.path.isfile(lang_file_path):
    lang_file_path = "lang/output-en.json"

with open(lang_file_path, "r", encoding="utf-8") as lang_file:
    lang_data = json.load(lang_file)

def get_response(key):
    if key in lang_data:
        return lang_data[key]
    else:
        return ""

def downloadfile(url, name):
    try:
        urllib.request.urlretrieve(url, name)
        print(get_response("download_success").format(name))
    except urllib.error.URLError:
        print(get_response("download_failure").format(name))

def wrongAnswer():
    print(get_response("invalid_value"))
    quit()

sinav_secimi = int(input(get_response("select_exam")))
if sinav_secimi == 1:
    sinav_secimi = "TYT"
elif sinav_secimi == 2:
    sinav_secimi = "AYT"
elif sinav_secimi == 3:
    sinav_secimi = "YDT"
else:
    wrongAnswer()

# Bruh wincort
if platform.system() == 'Windows':
    cortmode = 1
    folders = "\\"
else:
    cortmode = 0
    folders = "/"

def downloadQuestions(dirname, soru_link, i):
    file_name = get_response("question_file").format(i + 1)
    file_path = os.path.join(dirname, file_name)
    if os.path.exists(file_path):
        print(get_response("file_already_exists").format(file_name))
    else:
        downloadfile(soru_link, file_path)

def fetchLink(path, answer):
    link = base._replace(path=path + answer).geturl()
    baselink = requests.get(link)
    linkJson = baselink.json()
    return linkJson

def sanitize_folder_name(folder_name):
    sanitized_name = re.sub(r'[<>:"/\\|?*]', '', folder_name)
    return sanitized_name.strip()

sinavJson = fetchLink("/api/uc-adim-ders-listele/", sinav_secimi)

for i, sinav in enumerate(sinavJson, start=1):
    ders_baslik = sinav["baslik"]
    ders_id = sinav["id"]
    print(str(i), "-", sinav_secimi, ders_baslik)

ders_secimi = int(input(get_response("select_subject")))
if ders_secimi > len(sinavJson) or ders_secimi <= 0:
    wrongAnswer()

ders = sinavJson[ders_secimi-1]["id"]
ders_baslik = sinavJson[ders_secimi-1]["baslik"]

konuJson = fetchLink("/api/uc-adim-konu-listele/" + str(ders) + "-", sinav_secimi)

down = 1

if down == 1:
    adim = 3
    for konu in konuJson:
        konu_id = konu["id"]
        konuAdi = konu["ucAdimKonu"]
        sanitized_konuAdi = sanitize_folder_name(konuAdi)

        adim_folder_name = get_response("step_folder").format(adim)

        if cortmode:
            dirname = os.path.join(os.environ['USERPROFILE'], "Videos", str(sanitized_konuAdi) + " - " + adim_folder_name)
        else:
            dirname = os.path.join(str(os.getcwd()), str(sanitized_konuAdi) + " - " + adim_folder_name)

        os.makedirs(dirname, exist_ok=True)
        soruliste_link = soruliste._replace(query="kategori=" + str(sinav_secimi) + "&" + "konu=" + str(konu_id) + "&" + "adim=" + str(adim)).geturl()
        soruliste_json = requests.get(soruliste_link).json()
        for i, soru in enumerate(soruliste_json, start=1):
            soru_dosya = soru["dosya"]
            soru_link = base._replace(path="panel/upload/ucadim/" + soru_dosya).geturl()
            downloadQuestions(dirname, soru_link, i)
        print(get_response("test_folder_location").format(dirname))

print("\n" + get_response("exit_instructions"))

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
