# Generated by Django 2.2 on 2019-04-08 15:47

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Thread', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='link_preview_img',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='redditclone/media/'), upload_to='', verbose_name='Link Preview Image'),
        ),
    ]