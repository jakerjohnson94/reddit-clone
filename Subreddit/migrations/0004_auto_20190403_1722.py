# Generated by Django 2.2 on 2019-04-03 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subreddit', '0003_auto_20190402_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subreddit',
            name='description',
            field=models.CharField(max_length=250, verbose_name='Description'),
        ),
    ]
