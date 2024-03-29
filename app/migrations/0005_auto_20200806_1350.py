# Generated by Django 3.0.8 on 2020-08-06 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200805_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
                ('posted', models.DateField(default=datetime.datetime.now)),
                ('closing', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
