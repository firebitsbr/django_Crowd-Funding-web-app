# Generated by Django 3.0.3 on 2020-03-21 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_auto_20200320_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='login/static/e88f0054-e629-4232-b589-ff492df20435'),
        ),
    ]