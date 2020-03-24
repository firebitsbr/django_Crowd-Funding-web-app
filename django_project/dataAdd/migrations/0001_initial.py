# Generated by Django 3.0.3 on 2020-03-20 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0007_auto_20200320_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataAdd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthdate', models.DateField(blank=True)),
                ('country', models.CharField(blank=True, max_length=40)),
                ('facebookprofile', models.TextField(blank=True, default=' ')),
                ('user_id', models.ForeignKey(default=21, on_delete=django.db.models.deletion.CASCADE, to='login.User')),
            ],
        ),
    ]
