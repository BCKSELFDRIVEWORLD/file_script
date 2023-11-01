import os
import shutil

class DosyaIslemleri:
    def __init__(self, klasor_yollari, hedef_klasor):
        self.klasor_yollari = klasor_yollari
        self.hedef_klasor = hedef_klasor
        self.dosyalar = {}
        self.ayni_dosyalar = set()
        self.uzantilar = [".txt", ".yaml", ".pbstream", ".pgm", "_150px.png" ,".png"]

    def dosyalari_listele(self, dizin_yolu):
        if os.path.exists(dizin_yolu) and os.path.isdir(dizin_yolu):
            dosyalar = [os.path.splitext(dosya)[0] for dosya in os.listdir(dizin_yolu) if os.path.isfile(os.path.join(dizin_yolu, dosya))]
            return dosyalar
        else:
            return []

    def klasorlerdeki_dosyalari_tara(self):
        for klasor_yolu in self.klasor_yollari:
            self.dosyalar[klasor_yolu] = self.dosyalari_listele(klasor_yolu)

    def ayni_dosyalari_bul(self):
        self.ayni_dosyalar = set.intersection(*(set(degiskenler) for degiskenler in self.dosyalar.values()))

    def klasorler_olustur(self):
        for dosya_adi in self.ayni_dosyalar:
            os.makedirs(os.path.join(self.hedef_klasor, dosya_adi), exist_ok=True)

    def dosyalari_kopyala(self):
        ayni_dosyalar_liste = list(self.ayni_dosyalar)
        for dosya_adi in ayni_dosyalar_liste:
            for uzanti in self.uzantilar:
                dosya = dosya_adi + uzanti
                for klasor_yolu in self.klasor_yollari:
                    dosya_kaynak_yolu = os.path.join(klasor_yolu, dosya)  
                    if os.path.exists(dosya_kaynak_yolu):
                        dosya_hedef_klasor = os.path.join(self.hedef_klasor, dosya_adi)
                        dosya_hedef_yolu = os.path.join(dosya_hedef_klasor, dosya)
                        if not os.path.exists(dosya_hedef_klasor):
                            os.makedirs(dosya_hedef_klasor, exist_ok=True)
                        shutil.copy(dosya_kaynak_yolu, dosya_hedef_yolu)
                        break

# Dosya işlemleri için sınıfın örneklenmesi
klasor_yollari = [
    "/home/bck/maps_old/pgms",
    "/home/bck/maps_old/pbstreams",
    "/home/bck/maps_old/compressed",
    "/home/bck/maps_old/pngs",
    "/home/bck/maps_old"
]

hedef_klasor = "/home/bck/scripts_new"

dosya_islemleri = DosyaIslemleri(klasor_yollari, hedef_klasor)
dosya_islemleri.klasorlerdeki_dosyalari_tara()
dosya_islemleri.ayni_dosyalari_bul()
dosya_islemleri.klasorler_olustur()
dosya_islemleri.dosyalari_kopyala()
