# Generated by Django 4.2.8 on 2024-01-23 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='islogin',
            field=models.BooleanField(default=False, verbose_name='Girişli Kullanıcı'),
        ),
    ]
