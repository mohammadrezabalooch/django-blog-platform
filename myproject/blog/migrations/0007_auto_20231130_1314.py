# Generated by Django 2.2.5 on 2023-11-30 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20230906_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='آدرس آی پی')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', to='blog.IPAddress', verbose_name='بازدید ها'),
        ),
    ]
