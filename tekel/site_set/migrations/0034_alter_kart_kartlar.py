# Generated by Django 3.2.22 on 2023-11-17 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_set', '0033_alter_urunler_page_aciklama'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kart',
            name='kartlar',
            field=models.TextField(blank=True, help_text='Kart Açıklama', max_length=400, null=True, verbose_name='İletişim  Formu'),
        ),
    ]
