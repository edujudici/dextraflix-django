# Generated by Django 3.0.4 on 2020-03-26 15:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('video_date', models.DateField(default=datetime.date.today)),
                ('url', models.URLField()),
                ('description', models.TextField()),
                ('hashtags', models.CharField(max_length=255)),
                ('authors', models.ManyToManyField(to='video.Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Category')),
            ],
        ),
    ]
