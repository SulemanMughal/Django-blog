# Generated by Django 2.0.4 on 2019-04-21 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0015_auto_20190421_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='post_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
