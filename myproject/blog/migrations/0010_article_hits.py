# Generated by Django 2.2.5 on 2023-12-03 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_articlehit'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', through='blog.ArticleHit', to='blog.IPAddress', verbose_name='بازدید ها'),
        ),
    ]
