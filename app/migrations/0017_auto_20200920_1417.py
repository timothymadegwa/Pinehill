# Generated by Django 3.0.8 on 2020-09-20 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_talentpool'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='hobbies',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='linkedin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
