# Generated by Django 2.0.4 on 2019-04-21 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_auto_20190421_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='link',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
    ]
