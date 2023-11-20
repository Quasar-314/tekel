# models.py

from django.db import models
from django.utils.html import format_html
from ckeditor.fields import RichTextField
from django import forms



class PhoneNumber(models.Model):
    number = models.CharField(max_length=11)

    class Meta : 
        verbose_name = 'Telefon Numarası'
        verbose_name_plural = 'Telefon No'
        
    def __str__(self):
        return self.number

class WhatsAppNumber(models.Model):
    number = models.CharField(max_length=200)   
    
    class Meta : 
        verbose_name = 'WhatsApp Numarası'
        verbose_name_plural = 'WhatsApp No' 

    def __str__(self):
        return self.number

class Adres(models.Model):
    address = models.CharField(max_length=200)
    
    class Meta : 
        verbose_name = 'Açık Adres Yaz'
        verbose_name_plural = 'Adres Gir'

    def __str__(self):
        return self.address



class SosyalMedyaInsgr(models.Model):
    link = models.CharField(max_length=400)
    
    
    class Meta : 
        verbose_name = 'Instagram Link Gir'
        verbose_name_plural = 'Instagram'

    def __str__(self):
        return self.link

class KonumLink(models.Model):
    link = models.CharField(max_length=400)


    class Meta : 
        verbose_name = 'Konum Linki Gir'
        verbose_name_plural = 'Konum Link'
        
        
    def __str__(self):
        return self.link


class Galeri(models.Model):
    adlandir = models.CharField(max_length=100, blank=True, null=True, verbose_name="Görseli Adlandır", help_text="Lütfen Bir İsim Verin")
    resim = models.ImageField(upload_to='banner/', blank=True, null=True, verbose_name="Sayfaya resim Ekleyiniz")
    etiket =  models.CharField(max_length=400)   
    id_numara =  models.BigIntegerField(null=True)
    
    
    class Meta : 
        verbose_name = 'Galeri Resim Ekleme'
        verbose_name_plural = 'Galeri'
    
    def __str__(self):
        return self.adlandir if self.adlandir else "No Image"

class Urunler(models.Model):
    kategori = models.CharField(max_length=400)
    marka = models.CharField(max_length=400)
    açıklama = models.TextField(max_length=400, blank=True, null=True, verbose_name="Açıklama", help_text="Ürünler Açıklama")
    resim = models.ForeignKey(Galeri, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Ürün Ekleme", help_text="Ürün Resimleri")
    etiket =  models.CharField(max_length=400)
    
    class Meta : 
        verbose_name = 'Ürün Ekleme'
        verbose_name_plural = 'Ürünler'
    
    def __str__(self):
        return self.kategori
    
class Urunler_page(models.Model):
    baslik = models.CharField(max_length=400)
    baslik2 = models.CharField(max_length=400)
    aciklama = models.TextField(max_length=400, blank=True, null=True, verbose_name="Açıklama", help_text="Hakkımızda Açıklama")


    class Meta : 
        verbose_name = 'Ürünler Sayfa Başlık'
        verbose_name_plural = 'Ürünler Sayfa'
        
        
    def __str__(self):
        return self.baslik


class Banner(models.Model):
    baslik1 = models.CharField(max_length=400)
    baslik2 = models.CharField(max_length=400)
    aciklama = models.TextField(max_length=400, blank=True, null=True, verbose_name="Açıklama", help_text="Hakkımızda Açıklama")
    sayfa_sirasi = models.BigIntegerField(null=True)
    resim = models.ForeignKey(Galeri, on_delete=models.CASCADE, blank=False, null=False, verbose_name="Banner", help_text="Resminizi Seçiniz")
    urunler_link = models.ForeignKey(Urunler,on_delete=models.CASCADE, blank=False, null=False, verbose_name="Ürünü Seçin", help_text="Ürün Linki" )
    Whatsapp_Numara = models.ForeignKey(WhatsAppNumber,on_delete=models.CASCADE, blank=False, null=False, verbose_name="Whatsapp Numarası", help_text="Whatsapp Numarası Seç" )
    etiket =  models.CharField(max_length=400)    
    
    
    class Meta : 
        verbose_name = 'Slide Banner Bölümü'
        verbose_name_plural = 'Slide'
    
    def __str__(self):
        return self.resim.adlandir if self.resim and self.resim.adlandir else "No Image"


class About(models.Model):
    baslik1 = models.CharField(max_length=400)
    baslik2 = models.CharField(max_length=400)
    aciklama = models.TextField(max_length=400, blank=True, null=True, verbose_name="Açıklama", help_text="Anasayfa Açıklama")
    aciklama2 = models.TextField(max_length=400, blank=True, null=True, verbose_name="Açıklama2", help_text="Hakkımızda Açıklama")
    def __str__(self):
        return self.baslik1
    
    class Meta : 
        verbose_name = 'Hakkımızda Sayfa'
        verbose_name_plural = 'Hakımızda Bölümü'

class About_Video(models.Model):
    baslık = models.CharField(max_length=400,blank=True, null=True, verbose_name="Adlandır", help_text="video için bir isim ver ")
    video = models.FileField(upload_to='banner/', blank=True, null=True, verbose_name="video ekle", help_text="video ekeleme")
    etiket =  models.CharField(max_length=400)
    
    class Meta : 
        verbose_name = 'Hakkımızda Video'
        verbose_name_plural = 'Hakkımızda Video'
        
        
    def __str__(self):
        return self.baslık







class Alkoller(models.Model):
    baslik = models.CharField(max_length=400)
    aciklama = models.TextField(max_length=400, blank=True, null=True, verbose_name="Açıklama", help_text="Alkoller Açıklama")
    resim = models.ForeignKey(Galeri, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Ürün Ekleme", help_text="Ürünlerinizi Seçiniz")
    etiket =  models.CharField(max_length=400)
    
    
    class Meta : 
        verbose_name = 'Alkoller Anasayfa'
        verbose_name_plural = 'Alkoller Anasayfa'
        
        
    def __str__(self):
        return self.baslik

class GaleriBaslik(models.Model):
    baslik = models.CharField(max_length=400)
    aciklama = models.TextField(max_length=400, blank=True, null=True, verbose_name="Açıklama", help_text="Galeri Başlık Açıklama")


    class Meta : 
        verbose_name = 'Galeri Başlık'
        verbose_name_plural = 'Galeri Başlık'
    def __str__(self):
        return self.baslik

class DukkanResmi(models.Model):
    baslik = models.CharField(max_length=400,blank=True, null=True,)
    aciklama = models.TextField(max_length=400, blank=True, null=True, verbose_name="Açıklama", help_text="Galeri Açıklama")
    resim = models.ForeignKey(Galeri, on_delete=models.CASCADE, blank=True, null=True, verbose_name="İşlerme Resimleri", help_text="İşletme Resminizi")
    ID_numarasi = models.BigIntegerField(null=True)
    etiket =  models.CharField(max_length=400)
    def __str__(self):
        return self.baslik
    
    class Meta : 
        verbose_name = 'Dükkan Resmi Anasayfa'
        verbose_name_plural = 'Dükkan Resmi'





class Kart(models.Model):
    baslik = models.CharField(max_length=400)
    resim = models.ForeignKey(Galeri, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Loğo Ekleme", help_text="Logonuzu Seçiniz")
    kartlar = models.TextField(max_length=400, blank=True, null=True, verbose_name="İletişim  Formu", help_text="Kart Açıklama")
    sayfa_sirasi = models.BigIntegerField(null=True)
    etiket =  models.CharField(max_length=400)
    
    
    class Meta : 
        verbose_name = 'Anasayfa Kart'
        verbose_name_plural = 'Kart Anasayfa'
    
    def __str__(self):
        return self.baslik
    
    
    
"""
class Site_Resim(models.Model):
    intro = models.ForeignKey(Galeri, on_delete=models.CASCADE, blank=True, null=True, verbose_name="İntro Ekleme", help_text="İntro Seçiniz")    
    logo  = models.ForeignKey(Galeri, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Loğo Ekleme", help_text="Logonuzu Seçiniz")  
    resim1 = models.ForeignKey(Galeri, on_delete=models.CASCADE, blank=True, null=True, verbose_name="1.Resim Ekleme", help_text="1.Resmi Seçiniz")  
    resim2 = models.ForeignKey(Galeri, on_delete=models.CASCADE, blank=True, null=True, verbose_name="2.Resim Ekleme", help_text="2.Resmi Seçiniz")       
    resim3 = models.ForeignKey(Galeri, on_delete=models.CASCADE, blank=True, null=True, verbose_name="3.Resim Ekleme", help_text="3.Resmi Seçiniz") 
"""