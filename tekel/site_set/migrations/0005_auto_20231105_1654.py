# Generated by Django 3.2.22 on 2023-11-05 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_set', '0004_makale_yazar'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Makale',
        ),
        migrations.DeleteModel(
            name='Yazar',
        ),
    ]
