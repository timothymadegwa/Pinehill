# Generated by Django 3.0.8 on 2020-08-07 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200807_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(default='enter_slug_without_spaces', max_length=100, unique=True),
        ),
    ]