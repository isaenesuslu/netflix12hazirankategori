# Generated by Django 4.2.8 on 2024-01-21 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0005_contents_slug_alter_contents_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contents',
            name='slug',
            field=models.SlugField(null=True, verbose_name='Tür'),
        ),
        migrations.AlterField(
            model_name='contents',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Film Adı'),
        ),
    ]
