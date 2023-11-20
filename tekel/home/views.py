from django.shortcuts import render
from  site_set .models import *
from django.http.response import HttpResponse
def sozluklar():
    sozluk_sonuc = {}
    sozluk_sonuc["adres"] = Adres.objects.last()
    sozluk_sonuc["link"] = KonumLink.objects.last()
    sozluk_sonuc["whatsapp"] = WhatsAppNumber.objects.last()
    sozluk_sonuc["telefon"] = PhoneNumber.objects.last()
    sozluk_sonuc["instagram"] = SosyalMedyaInsgr.objects.last()
    
    
    return sozluk_sonuc
def index(request):

    tel_numara = PhoneNumber.objects.first()
    wp_numara = WhatsAppNumber.objects.first()
    adres = Adres.objects.first() 
    instagram_link = SosyalMedyaInsgr.objects.first()
    bannerlerim_query = Banner.objects.all().order_by("sayfa_sirasi")[:3]
    hakkinda = About.objects.all()
    hakkinda_video = About_Video.objects.all()
    alkoller_resim = Alkoller.objects.all()
    galeri_baslik = GaleriBaslik.objects.all()
    galeri_resim= Galeri.objects.all()
    urun_resim= Urunler.objects.all()
    konum = KonumLink.objects.first()
    kart = Kart.objects.all() 
    urunler_page = Urunler_page.objects.all()
    dukkan_resim = DukkanResmi.objects.all()
    

    context = {
               
        "tel_numara": tel_numara,
        "wp_numara": wp_numara,
        "adres": adres,   
        "instagram_link": instagram_link,
        "bannerlerim": bannerlerim_query,
        "hakkinda": hakkinda,
        "hakkinda_video": hakkinda_video,
        "alkoller_resim": alkoller_resim,
        "galeri_baslik": galeri_baslik,
        "galeri_resim": galeri_resim,
        "urun_resim": urun_resim,
        "konum": konum,
        "kart": kart, 
        "dukkan_resim" : dukkan_resim,
        "urunler_page" :urunler_page,
        "site_bilgileri" : sozluklar()
        
    }

    return render(request, "home_page/index.html", context)




def galery (request):    
    galeri_resim= Galeri.objects.all()
   
    context = {
              "galeri_resim": galeri_resim,
             "site_bilgileri" : sozluklar(),
    }
    return render(request, "galery_page/index.html", context)



def about (request):
    galeri_resim= Galeri.objects.all()
    hakkinda = About.objects.all()
    
    context = {"galeri_resim": galeri_resim,
              "hakkinda": hakkinda,
              "site_bilgileri" : sozluklar(),
    }
    return render(request, "hakkımızda_page/index.html", context)



def products (request):
    urunler_page = Urunler_page.objects.all()
    urun_resim= Urunler.objects.all()
    context = {
               "urun_resim": urun_resim,
               "urunler_page" :urunler_page,
               "site_bilgileri" : sozluklar(),
    }
    return render(request, "ürünler_page/index.html", context)