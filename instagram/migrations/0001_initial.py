# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-05-20 12:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=250)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('image_name', models.CharField(max_length=40)),
                ('image_caption', models.CharField(max_length=40, null=True)),
                ('image_location', models.CharField(max_length=40, null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('likes', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('bio', models.CharField(max_length=40)),
                ('profile_pic', models.ImageField(upload_to='profile/')),
                ('pub_date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('followers', models.ManyToManyField(blank=True, related_name='followers_profile', to='instagram.Profile')),
                ('following', models.ManyToManyField(blank=True, related_name='following_profile', to='instagram.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='Profile',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='instagram.Profile'),
        ),
        migrations.AddField(
            model_name='image',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='instagram.Image'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
