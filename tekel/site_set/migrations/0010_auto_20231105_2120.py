# Generated by Django 3.2.22 on 2023-11-05 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_set', '0009_rename_konumnavigasyon_konum_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='whatshappno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whatshapp_numarasi', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='numara',
            name='sirket_numarasi',
            field=models.PositiveIntegerField(),
        ),
    ]
