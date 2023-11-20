# admin property
from django.contrib import admin
from .models import *



admin.site.register(PhoneNumber)
admin.site.register(WhatsAppNumber)
admin.site.register(Adres)
admin.site.register(SosyalMedyaInsgr)
admin.site.register(KonumLink)
admin.site.register(Galeri)
admin.site.register(Banner)
admin.site.register(About)
admin.site.register(About_Video)
admin.site.register(Urunler)
admin.site.register(Alkoller)
admin.site.register(GaleriBaslik)
admin.site.register(DukkanResmi)
admin.site.register(Kart)
admin.site.register(Urunler_page)









"""
class SiteAdiAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('number',)
    search_fields = ['number']

class WhatsAppNumberAdmin(admin.ModelAdmin):
    list_display = ('number',)

@admin.register(Adres)
class AdresAdmin(admin.ModelAdmin):
    list_display = ('address',)

@admin.register(SosyalMedyaFb)
class SosyalMedyaFbAdmin(admin.ModelAdmin):
    list_display = ('link',)

@admin.register(SosyalMedyaInsgr)
class SosyalMedyaInsgrAdmin(admin.ModelAdmin):
    list_display = ('link',)

@admin.register(KonumLink)
class KonumLinkAdmin(admin.ModelAdmin):
    list_display = ('link',)

@admin.register(Galeri)
class GaleriAdmin(admin.ModelAdmin):
    list_display = ('adlandir',)

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('sayfa_sirasi', 'get_galeri_adlandir')

    def get_galeri_adlandir(self, obj):
        return obj.resim.adlandir if obj.resim and obj.resim.adlandir else "No Image"

    get_galeri_adlandir.short_description = "Galeri Adı"

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('baslik1', 'baslik2')

@admin.register(AboutVideo)
class AboutVideoAdmin(admin.ModelAdmin):
    list_display = ('video',)

@admin.register(AlkolBaslik)
class AlkolBaslikAdmin(admin.ModelAdmin):
    list_display = ('baslik',)

@admin.register(Alkoller)
class AlkollerAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'aciklama','resim')

@admin.register(GaleriBaslik)
class GaleriBaslikAdmin(admin.ModelAdmin):
    list_display = ('baslik',)

@admin.register(DukkanResmi)
class DukkanResmiAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'ID_numarasi')

@admin.register(Urunler)
class UrunlerAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'aciklama')

@admin.register(SayfaLogosu)
class SayfaLogosuAdmin(admin.ModelAdmin):
    list_display = ('resim',)



@admin.register(Kart)
class KartAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_kart_preview')
    search_fields = ['id']

    def get_kart_preview(self, obj):
        return obj.kartlar[:50]  # Önizleme olarak ilk 50 karakteri göster

    get_kart_preview.short_description = 'Kart Önizleme'
"""