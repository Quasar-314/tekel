# Generated by Django 3.2.22 on 2023-11-12 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_set', '0023_auto_20231112_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='Whatsapp_Numara',
            field=models.ForeignKey(default=1, help_text='Ürün Linki', on_delete=django.db.models.deletion.CASCADE, to='site_set.whatsappnumber', verbose_name='Ürünü Seçin'),
            preserve_default=False,
        ),
    ]
