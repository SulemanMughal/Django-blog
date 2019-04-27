# Generated by Django 2.2 on 2019-04-25 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0019_auto_20190425_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.BlogComment')),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
    ]
