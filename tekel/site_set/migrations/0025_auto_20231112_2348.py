# Generated by Django 3.2.22 on 2023-11-12 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_set', '0024_banner_whatsapp_numara'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutvideo',
            name='etiket',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alkoller',
            name='etiket',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='banner',
            name='etiket',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dukkanresmi',
            name='etiket',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galeri',
            name='etiket',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kart',
            name='etiket',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sayfalogosu',
            name='etiket',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='urunler',
            name='etiket',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
    ]
