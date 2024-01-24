# Generated by Django 4.2.8 on 2024-01-21 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contents',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='content',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.contents', verbose_name='Kategori'),
        ),
    ]
