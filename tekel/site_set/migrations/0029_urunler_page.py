# Generated by Django 3.2.22 on 2023-11-16 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_set', '0028_auto_20231116_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='Urunler_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('başlık', models.CharField(max_length=400)),
                ('açıklama', models.CharField(max_length=400)),
            ],
        ),
    ]
