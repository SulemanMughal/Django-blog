# Generated by Django 2.0.4 on 2019-04-21 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0011_remove_blog_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogauthor',
            name='image',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
