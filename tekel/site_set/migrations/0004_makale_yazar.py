# Generated by Django 3.2.22 on 2023-11-05 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_set', '0003_auto_20231105_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yazar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=100)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Makale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('başlık', models.CharField(max_length=200)),
                ('içerik', models.TextField()),
                ('tarih', models.DateTimeField(auto_now_add=True)),
                ('yazar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_set.yazar')),
            ],
        ),
    ]
