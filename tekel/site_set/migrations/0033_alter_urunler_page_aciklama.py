# Generated by Django 3.2.22 on 2023-11-16 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_set', '0032_auto_20231116_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urunler_page',
            name='aciklama',
            field=models.TextField(blank=True, help_text='Hakkımızda Açıklama', max_length=400, null=True, verbose_name='Açıklama'),
        ),
    ]
