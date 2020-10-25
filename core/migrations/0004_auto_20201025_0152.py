# Generated by Django 3.1.2 on 2020-10-24 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_article_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='short_description',
            field=models.TextField(blank=True, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(verbose_name='Текст статьи'),
        ),
    ]
