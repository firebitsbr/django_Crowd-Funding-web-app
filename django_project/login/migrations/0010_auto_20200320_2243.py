# Generated by Django 3.0.3 on 2020-03-20 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20200320_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='login/static/70a8885b-f6d4-4a75-a2a1-dfa6581593a3'),
        ),
    ]
