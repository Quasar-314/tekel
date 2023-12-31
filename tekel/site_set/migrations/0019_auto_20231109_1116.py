# Generated by Django 3.2.22 on 2023-11-09 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_set', '0018_alter_galeri_resim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutvideo',
            name='video',
            field=models.ForeignKey(blank=True, help_text='video Seçiniz', null=True, on_delete=django.db.models.deletion.CASCADE, to='site_set.galeri', verbose_name='Video'),
        ),
        migrations.AlterField(
            model_name='alkoller',
            name='resim',
            field=models.ForeignKey(blank=True, help_text='Ürünlerinizi Seçiniz', null=True, on_delete=django.db.models.deletion.CASCADE, to='site_set.galeri', verbose_name='Ürün Ekleme'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='resim',
            field=models.ForeignKey(blank=True, help_text='Resminizi Seçiniz', null=True, on_delete=django.db.models.deletion.CASCADE, to='site_set.galeri', verbose_name='Banner'),
        ),
        migrations.AlterField(
            model_name='dukkanresmi',
            name='resim',
            field=models.ForeignKey(blank=True, help_text='İşletme Resminizi', null=True, on_delete=django.db.models.deletion.CASCADE, to='site_set.galeri', verbose_name='İşlerme Resimleri'),
        ),
        migrations.AlterField(
            model_name='urunler',
            name='resim',
            field=models.ForeignKey(blank=True, help_text='Ürün Resimleri', null=True, on_delete=django.db.models.deletion.CASCADE, to='site_set.galeri', verbose_name='Ürün Ekleme'),
        ),
    ]
