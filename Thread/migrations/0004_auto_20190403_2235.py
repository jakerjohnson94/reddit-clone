# Generated by Django 2.2 on 2019-04-03 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Thread', '0003_thread_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
    ]