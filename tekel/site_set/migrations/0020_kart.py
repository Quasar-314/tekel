# Generated by Django 3.2.22 on 2023-11-11 19:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_set', '0019_auto_20231109_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kartlar', ckeditor.fields.RichTextField(blank=True, max_length=400, null=True)),
            ],
        ),
    ]