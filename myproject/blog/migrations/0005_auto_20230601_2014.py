# Generated by Django 2.2.5 on 2023-06-01 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20230405_0428'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['parent__id', 'position'], 'verbose_name': 'Category'},
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
    ]
