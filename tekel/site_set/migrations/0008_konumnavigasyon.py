# Generated by Django 3.2.22 on 2023-11-05 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_set', '0007_auto_20231105_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='konumnavigasyon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=400)),
            ],
        ),
    ]