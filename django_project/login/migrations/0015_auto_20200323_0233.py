# Generated by Django 3.0.3 on 2020-03-23 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_auto_20200322_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='login/static/e60b4836-66c1-4ec7-94f4-16929733b79c'),
        ),
    ]
