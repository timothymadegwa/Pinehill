# Generated by Django 3.0.8 on 2020-08-17 11:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200807_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='body',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='image',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='blogs/images'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='blogs/images'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='blogs/images'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='paragraph_1',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='paragraph_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='paragraph_3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
