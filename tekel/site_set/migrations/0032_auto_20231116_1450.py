# Generated by Django 3.2.22 on 2023-11-16 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_set', '0031_auto_20231116_1450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urunler_page',
            old_name='başlik',
            new_name='baslik',
        ),
        migrations.RenameField(
            model_name='urunler_page',
            old_name='başlik2',
            new_name='baslik2',
        ),
    ]