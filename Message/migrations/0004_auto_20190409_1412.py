# Generated by Django 2.2 on 2019-04-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RedditUser', '0001_initial'),
        ('Message', '0003_message_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='notification',
        ),
        migrations.AddField(
            model_name='message',
            name='notification',
            field=models.ManyToManyField(blank=True, related_name='notification', to='RedditUser.RedditUser', verbose_name='Notification'),
        ),
    ]
