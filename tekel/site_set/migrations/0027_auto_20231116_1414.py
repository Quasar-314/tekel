# Generated by Django 3.2.22 on 2023-11-16 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_set', '0026_alter_banner_whatsapp_numara'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='aciklama2',
            field=models.TextField(blank=True, help_text='Hakkımızda Açıklama', max_length=400, null=True, verbose_name='Açıklama2'),
        ),
        migrations.AlterField(
            model_name='about',
            name='aciklama',
            field=models.TextField(blank=True, help_text='Anasayfa Açıklama', max_length=400, null=True, verbose_name='Açıklama'),
        ),
    ]