# Generated by Django 3.0.8 on 2020-08-07 08:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200806_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]