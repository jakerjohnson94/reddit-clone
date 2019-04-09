# Generated by Django 2.2 on 2019-04-09 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MessageThread', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagethread',
            name='title',
            field=models.CharField(default='w', max_length=50, verbose_name='TIle'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='messagethread',
            name='messages',
            field=models.ManyToManyField(blank=True, to='Message.Message', verbose_name='Messages'),
        ),
    ]
