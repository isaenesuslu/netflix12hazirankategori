# Generated by Django 4.2.8 on 2024-01-21 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0006_alter_contents_slug_alter_contents_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='contents',
            name='ispopular',
            field=models.BooleanField(default=False, verbose_name='Yeni Eklenmiş'),
        ),
    ]
