# Generated by Django 3.2.22 on 2023-11-16 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_set', '0029_urunler_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='urunler_page',
            name='başlık2',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
    ]
