# Generated by Django 2.0.4 on 2019-04-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_auto_20190421_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='video_link',
            field=models.CharField(max_length=1000),
        ),
    ]
