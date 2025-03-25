from django.db import models
from apps.staff import models

class Tur(models.Model):
    ad = models.CharField(max_length=100, unique=True)
    kisaltma = models.CharField(max_length=10, unique=True)  
    def __str__(self):
        return f"{self.name} ({self.initial})"

class Usul(models.Model):
    ad = models.CharField(max_length=250, unique=True) 
    kisaltma = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return f"{self.name}"

class ZorunluPersonel(models.Model):
    pozisyon = models.CharField(max_length=250)
    mesleki_unvan = models.CharField(max_length=250)
    mesleki_ozellikleri = models.CharField(max_length=250)

class Ihale(models.Model):
    DIGER_HUSUSLAR_SECENEK = [
        ('yapim', f"Bahse konu işe ait diğer hususlar (ihale bedeline dahil olan kalemler,yüklenicinin yükümlülükleri, teknik personeller, sorumlu olduğu diğer işler,diğer ceza hükümleri ve yapım işi ile ilgili teknik hususlar vb) ihale dökümanında yer alan {sartname_tarihi} tarihli Genel ve Teknik Şartnamede ayrıntılı olarak belirtilmiştir."),
        ('mal', f"Bahse konu işe ait diğer hususlar (ihale bedeline dahil olan kalemler,  yüklenicinin yükümlülükleri, teslim şartları, muayene, gerekli standart ve onaylara ilişkin belgeler, işle ilgili teknik hususlar vb) ihale dökümanında yer alan {sartname_tarihi} tarihli Genel ve Teknik Şartnamede ayrıntılı olarak belirtilmiştir."),
        ('hizmet', f"Bahse konu işe ait diğer hususlar (ihale bedeline dahil olan kalemler,  yüklenicinin yükümlülükleri, teslim şartları, gerekli standart ve onaylara ilişkin belgeler, işle ilgili teknik hususlar vb) ihale dökümanında yer alan {sartname_tarihi} tarihli Genel ve Teknik Şartnamede ayrıntılı olarak belirtilmiştir."),
        ('','')  
    ]

    uygulama_yili = models.DateField(blank=True, null=True)
    isin_adi = models.CharField(max_length=250) 
    aciklama = models.TextField(max_length=10000, blank=True,null=True) 
    isin_turu = models.ForeignKey(Tur,on_delete=models.CASCADE,related_name="Tür")
    ihale_usulu = models.ForeignKey(Usul,on_delete=models.CASCADE,related_name="Usül")
    olur_tarihi = models.DateField(blank=True,null=True)
    olur_sayisi = models.IntegerField(blank=True,null=True)
    sartname_tarihi = models.DateField(blank=True,null=True)
    isin_suresi = models.IntegerField(blank=True,null=True)
    yer_teslim_tarihi = models.DateField(blank=True,null=True)
    isin_baslangic_tarihi = models.DateField(blank=True,null=True)
    ihale_icin_yeterlilik_kriterleri =  models.TextField(blank=True,max_length=10000, null=True) 
    is_deneyim_orani =  models.IntegerField(blank=True,null=True, max_length=3)
    calismaya_uygun_olmayan_gun = models.CharField(blank=True,max_length=200, null=True) 
    odeme_dilimi = models.CharField(blank=True,max_length=200, null=True) 
    teminat_suresi = models.CharField(blank=True,max_length=200, null=True)
    gecikme_cezasi = models.CharField(blank=True,max_length=50, null=True)
    garanti =  models.TextField(blank=True,max_length=10000, null=True) 
    zorunlu_personel = models. ForeignKey(ZorunluPersonel,on_delete=models.CASCADE,related_name="Zorunlu Personel", blank=True,null=True)
    diger_hususlar=models.TextField(blank=True,max_length=10000, null=True, choices=DIGER_HUSUSLAR_SECENEK) 
    hazirlayan = models.ForeignKey(Staff,on_delete=models.CASCADE,related_name="Personel")
    gerceklestirme_gorevlisi = models.ForeignKey(Staff,on_delete=models.CASCADE,related_name="Personel")
    mudur = models.ForeignKey(Staff,on_delete=models.CASCADE,related_name="Personel")
    yaklasik_maliyet = models.FloatField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.isin_adi}"
    

class IsKalemleri(models.Model):
    BIRIMLER_SECENEK = [
        'm' ,
        'm2',
        'm3',
        'adet',
        'kg',
        'ton',
    ]

    poz_no = models.CharField(max_length=250, blank=True, null=True) 
    poz_adi = models.CharField(max_length=250)  
    poz_tarifi = models.TextField(max_length=5000, blank=True, null=True) 
    poz_birimi = models.CharField(choices=BIRIMLER_SECENEK) 
    poz_birim_fiyatı = models.FloatField(blank=True, null=True) 
    isin_adi = models.ForeignKey(Ihale, on_delete=models.CASCADE, related_name="Isın adi")


