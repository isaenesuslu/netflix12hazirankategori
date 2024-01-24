# Generated by Django 4.2.8 on 2024-01-21 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0004_remove_contents_category_contents_isnew_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contents',
            name='slug',
            field=models.SlugField(null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='contents',
            name='title',
            field=models.CharField(max_length=50, verbose_name='İçerik'),
        ),
    ]