# Generated by Django 4.2.8 on 2024-01-23 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0008_contents_islogin_alter_contents_ispopular'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contents',
            name='islogin',
        ),
    ]
