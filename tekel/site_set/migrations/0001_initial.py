# Generated by Django 3.2.22 on 2023-11-03 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sirket_adresi', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sayfa_sirasi', models.BigIntegerField(null=True)),
                ('baner_resim', models.FileField(blank=True, upload_to='banner/', verbose_name='Sayfaya resim Ekleyiniz')),
            ],
        ),
        migrations.CreateModel(
            name='email_adres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sirket_email_adresi', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='numara',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sirket_numarasi', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='sayfa_logosu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sayfa_logo', models.FileField(blank=True, null=True, upload_to='logo/', verbose_name='Sayfaya Logo Ekleyin')),
            ],
        ),
        migrations.CreateModel(
            name='sosyalmedyafb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='sosyalmedyaInsgr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='sosyalmedyalinkd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='sosyalmedyaTw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=400)),
            ],
        ),
    ]
