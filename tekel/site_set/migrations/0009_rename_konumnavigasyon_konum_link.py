# Generated by Django 3.2.22 on 2023-11-05 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_set', '0008_konumnavigasyon'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='konumnavigasyon',
            new_name='konum_link',
        ),
    ]