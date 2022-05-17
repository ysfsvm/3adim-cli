# Unoffical OGM 3 Adım Soru Bankası Çözüm Videoları Api
For basic functionality use `3adim_cli.py`

Credits: Burpsuite, wireshark and me.


#### USAGE

link: https://ogmmateryal.eba.gov.tr/api/uc-adim-konu-listele/kategoriler
````
OUTPUT:
[true,true,true]
````
usage: `https://ogmmateryal.eba.gov.tr/api/uc-adim-ders-listele/{sınav adı}`

link: https://ogmmateryal.eba.gov.tr/api/uc-adim-ders-listele/AYT
````
OUTPUT:
[
  {
    "id": 6,
    "sinifId": 7,
    "baslik": "Biyoloji",
    "sira": 1,
    "kod": "BIY",
    "ikon": "fas fa-dna",
    "eKitap": false,
    "soruHavuzu": false,
    "dersIdler": null,
    "sinifIdler": null,
    "urlKod": null
  },
  {
    "id": 9,
    "sinifId": 6,
    "baslik": "Coğrafya",
    "sira": 2,
    "kod": "COG",
    "ikon": "fas fa-globe-africa",
    "eKitap": false,
    "soruHavuzu": false,
    "dersIdler": null,
    "sinifIdler": null,
    "urlKod": null
  },
  {
    "id": 15,
    "sinifId": 8,
    "baslik": "Felsefe",
    "sira": 3,
    "kod": "FEL",
    "ikon": "far fa-question-circle",
    "eKitap": false,
    "soruHavuzu": false,
    "dersIdler": null,
    "sinifIdler": null,
    "urlKod": null
  },
  {
    "id": 32,
    "sinifId": 6,
    "baslik": "Fizik",
    "sira": 7,
    "kod": "FIZ",
    "ikon": "fas fa-atom",
    "eKitap": false,
    "soruHavuzu": false,
    "dersIdler": null,
    "sinifIdler": null,
    "urlKod": null
  },
  {
    "id": 44,
    "sinifId": 6,
    "baslik": "Kimya",
    "sira": 9,
    "kod": "KIM",
    "ikon": "fas fa-vial",
    "eKitap": false,
    "soruHavuzu": false,
    "dersIdler": null,
    "sinifIdler": null,
    "urlKod": null
  },
  {
    "id": 49,
    "sinifId": 7,
    "baslik": "Matematik",
    "sira": 11,
    "kod": "MAT",
    "ikon": "fas fa-drafting-compass",
    "eKitap": false,
    "soruHavuzu": false,
    "dersIdler": null,
    "sinifIdler": null,
    "urlKod": null
  },
  {
    "id": 55,
    "sinifId": 6,
    "baslik": "Tarih",
    "sira": 12,
    "kod": "TAR",
    "ikon": "fas fa-landmark",
    "eKitap": false,
    "soruHavuzu": false,
    "dersIdler": null,
    "sinifIdler": null,
    "urlKod": null
  },
  {
    "id": 58,
    "sinifId": 6,
    "baslik": "Türk Dili ve Edebiyatı",
    "sira": 13,
    "kod": "TDE",
    "ikon": "fas fa-pen-nib",
    "eKitap": false,
    "soruHavuzu": false,
    "dersIdler": null,
    "sinifIdler": null,
    "urlKod": null
  }
]
````

usage: `https://ogmmateryal.eba.gov.tr/api/uc-adim-konu-listele/{ders-id}-{sinav-adi}`

link: https://ogmmateryal.eba.gov.tr/api/uc-adim-konu-listele/6-TYT
````
OUTPUT:
[
  {
    "id": 955,
    "kategori": null,
    "sinifId": 0,
    "dersId": 5,
    "uniteId": 0,
    "konuId": 0,
    "adimNo": 0,
    "soruNo": 0,
    "dosya": null,
    "ucAdimKonu": "Canlıların Ortak Özellikleri - İnorganik Bileşikler"
  },
  {
    "id": 154,
    "kategori": null,
    "sinifId": 0,
    "dersId": 5,
    "uniteId": 0,
    "konuId": 0,
    "adimNo": 0,
    "soruNo": 0,
    "dosya": null,
    "ucAdimKonu": "Canlıların Sınıflandırılması - Canlı Âlemleri̇ ve Özellikleri"
  },
  {
    "id": 396,
    "kategori": null,
    "sinifId": 0,
    "dersId": 6,
    "uniteId": 0,
    "konuId": 0,
    "adimNo": 0,
    "soruNo": 0,
    "dosya": null,
    "ucAdimKonu": "Ekosistemde Madde ve Enerji Akışı- Madde Döngüleri"
  },
  {
    "id": 290,
    "kategori": null,
    "sinifId": 0,
    "dersId": 6,
    "uniteId": 0,
    "konuId": 0,
    "adimNo": 0,
    "soruNo": 0,
    "dosya": null,
    "ucAdimKonu": "Ekosistemin Canlı-Cansız Bileşenleri- Canlılardaki Beslenme İlişkileri"
  },
  {
    "id": 1187,
    "kategori": null,
    "sinifId": 0,
    "dersId": 5,
    "uniteId": 0,
    "konuId": 0,
    "adimNo": 0,
    "soruNo": 0,
    "dosya": null,
    "ucAdimKonu": "Enzimler - Vitaminler - Hormonlar"
  },
  {
    "id": 878,
    "kategori": null,
    "sinifId": 0,
    "dersId": 6,
    "uniteId": 0,
    "konuId": 0,
    "adimNo": 0,
    "soruNo": 0,
    "dosya": null,
    "ucAdimKonu": "Eş Baskınlık - Çok Alellilik Eşeye Bağlı Kalıtım"
  },
  {
    "id": 451,
    "kategori": null,
    "sinifId": 0,
    "dersId": 6,
    "uniteId": 0,
    "konuId": 0,
    "adimNo": 0,
    "soruNo": 0,
    "dosya": null,
    "ucAdimKonu": "Güncel Çevre Sorunları- Biyolojik Çeşitliliğin Korunması"
  },
  {
    "id": 1111,
    "kategori": null,
    "sinifId": 0,
    "dersId": 5,
    "uniteId": 0,
    "konuId": 0,
    "adimNo": 0,
    "soruNo": 0,
    "dosya": null,
    "ucAdimKonu": "Hücre Zarından Madde Geçişleri - Bilimsel Yöntem"
  },
  {
    "id": 1010,
    "kategori": null,
    "sinifId": 0,
    "dersId": 5,
    "uniteId": 0,
    "konuId": 0,
    "adimNo": 0,
    "soruNo": 0,
    "dosya": null,
    "ucAdimKonu": "Hücrenin Yapısı ve Kısımları"
  },
  {
    "id": 1028,
    "kategori": null,
    "sinifId": 0,
    "dersId": 5,
    "uniteId": 0,
    "konuId": 0,
    "adimNo": 0,
    "soruNo": 0,
    "dosya": null,
    "ucAdimKonu": "Karbonhidratlar - Lipitler - Proteinler"
  },
  {
    "id": 892,
    "kategori": null,
    "sinifId": 0,
    "dersId": 6,
    "uniteId": 0,
    "konuId": 0,
    "adimNo": 0,
    "soruNo": 0,
    "dosya": null,
    "ucAdimKonu": "Mayoz ve Eşeyli Üreme"
  },
  {
    "id": 183,
    "kategori": null,
    "sinifId": 0,
    "dersId": 6,
    "uniteId": 0,
    "konuId": 0,
    "adimNo": 0,
    "soruNo": 0,
    "dosya": null,
    "ucAdimKonu": "Mendel İlkeleri ve Uygulamaları"
  },
  {
    "id": 338,
    "kategori": null,
    "sinifId": 0,
    "dersId": 6,
    "uniteId": 0,
    "konuId": 0,
    "adimNo": 0,
    "soruNo": 0,
    "dosya": null,
    "ucAdimKonu": "Mitoz ve Eşeysiz Üreme"
  },
  {
    "id": 1260,
    "kategori": null,
    "sinifId": 0,
    "dersId": 5,
    "uniteId": 0,
    "konuId": 0,
    "adimNo": 0,
    "soruNo": 0,
    "dosya": null,
    "ucAdimKonu": "Nükleik Asitler - ATP"
  },
  {
    "id": 1069,
    "kategori": null,
    "sinifId": 0,
    "dersId": 6,
    "uniteId": 0,
    "konuId": 0,
    "adimNo": 0,
    "soruNo": 0,
    "dosya": null,
    "ucAdimKonu": "Soyağaçları - Genetik Varyasyonlar ve Biyolojik Çeşitlilik"
  }
]
````

usage: `https://ogmmateryal.eba.gov.tr/api/uc-adim-soru-listele?kategori={sinav-adi - (TYT,AYT,YDT)}&konu={konu-id}&adim={test-sayisi (1-2-3)}`

link: https://ogmmateryal.eba.gov.tr/api/uc-adim-soru-listele?kategori=TYT&konu=955&adim=1
````
OUTPUT:
[
  {
    "id": 2368,
    "kategori": "TYT",
    "sinifId": 6,
    "dersId": 5,
    "uniteId": 24,
    "konuId": 125,
    "adimNo": 1,
    "soruNo": 1,
    "dosya": "5dcn3d3rxmq.mp4",
    "ucAdimKonu": "Canlıların Ortak Özellikleri - İnorganik Bileşikler"
  },
  {
    "id": 2369,
    "kategori": "TYT",
    "sinifId": 6,
    "dersId": 5,
    "uniteId": 24,
    "konuId": 125,
    "adimNo": 1,
    "soruNo": 2,
    "dosya": "dlafu3nv0go.mp4",
    "ucAdimKonu": "Canlıların Ortak Özellikleri - İnorganik Bileşikler"
  },
  {
    "id": 955,
    "kategori": "TYT",
    "sinifId": 6,
    "dersId": 5,
    "uniteId": 24,
    "konuId": 125,
    "adimNo": 1,
    "soruNo": 3,
    "dosya": "juseylsqmlw.mp4",
    "ucAdimKonu": "Canlıların Ortak Özellikleri - İnorganik Bileşikler"
  },
  {
    "id": 957,
    "kategori": "TYT",
    "sinifId": 6,
    "dersId": 5,
    "uniteId": 24,
    "konuId": 125,
    "adimNo": 1,
    "soruNo": 4,
    "dosya": "0uzt1apocno.mp4",
    "ucAdimKonu": "Canlıların Ortak Özellikleri - İnorganik Bileşikler"
  },
  {
    "id": 959,
    "kategori": "TYT",
    "sinifId": 6,
    "dersId": 5,
    "uniteId": 24,
    "konuId": 126,
    "adimNo": 1,
    "soruNo": 5,
    "dosya": "b2pu3hbzlwt.mp4",
    "ucAdimKonu": "Canlıların Ortak Özellikleri - İnorganik Bileşikler"
  },
  {
    "id": 960,
    "kategori": "TYT",
    "sinifId": 6,
    "dersId": 5,
    "uniteId": 24,
    "konuId": 126,
    "adimNo": 1,
    "soruNo": 6,
    "dosya": "zxcfrbtzd5w.mp4",
    "ucAdimKonu": "Canlıların Ortak Özellikleri - İnorganik Bileşikler"
  },
  {
    "id": 963,
    "kategori": "TYT",
    "sinifId": 6,
    "dersId": 5,
    "uniteId": 24,
    "konuId": 126,
    "adimNo": 1,
    "soruNo": 7,
    "dosya": "lcfy0zhdmt2.mp4",
    "ucAdimKonu": "Canlıların Ortak Özellikleri - İnorganik Bileşikler"
  },
  {
    "id": 965,
    "kategori": "TYT",
    "sinifId": 6,
    "dersId": 5,
    "uniteId": 24,
    "konuId": 126,
    "adimNo": 1,
    "soruNo": 8,
    "dosya": "wctbx2iy20q.mp4",
    "ucAdimKonu": "Canlıların Ortak Özellikleri - İnorganik Bileşikler"
  },
  {
    "id": 967,
    "kategori": "TYT",
    "sinifId": 6,
    "dersId": 5,
    "uniteId": 24,
    "konuId": 126,
    "adimNo": 1,
    "soruNo": 9,
    "dosya": "yyvojrhrzzb.mp4",
    "ucAdimKonu": "Canlıların Ortak Özellikleri - İnorganik Bileşikler"
  },
  {
    "id": 968,
    "kategori": "TYT",
    "sinifId": 6,
    "dersId": 5,
    "uniteId": 24,
    "konuId": 125,
    "adimNo": 1,
    "soruNo": 10,
    "dosya": "suychbuspfl.mp4",
    "ucAdimKonu": "Canlıların Ortak Özellikleri - İnorganik Bileşikler"
  },
  {
    "id": 969,
    "kategori": "TYT",
    "sinifId": 6,
    "dersId": 5,
    "uniteId": 24,
    "konuId": 125,
    "adimNo": 1,
    "soruNo": 11,
    "dosya": "sxnzpwv1lpd.mp4",
    "ucAdimKonu": "Canlıların Ortak Özellikleri - İnorganik Bileşikler"
  },
  {
    "id": 1347,
    "kategori": "TYT",
    "sinifId": 6,
    "dersId": 5,
    "uniteId": 24,
    "konuId": 126,
    "adimNo": 1,
    "soruNo": 12,
    "dosya": "yt5tap5cbdb.mp4",
    "ucAdimKonu": "Canlıların Ortak Özellikleri - İnorganik Bileşikler"
  }
]
````

usage: `https://ogmmateryal.eba.gov.tr/panel/upload/ucadim/{dosya}`

output: raw mp4
