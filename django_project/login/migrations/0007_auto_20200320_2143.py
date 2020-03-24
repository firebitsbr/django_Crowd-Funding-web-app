# Generated by Django 3.0.3 on 2020-03-20 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20200314_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='login/static/ba2ae1a5-38b3-4bc3-a28f-0028d347791c'),
        ),
    ]