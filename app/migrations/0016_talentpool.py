# Generated by Django 3.0.8 on 2020-09-16 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_contact_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='TalentPool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('cv', models.FileField(upload_to='jobs/talent/cv')),
            ],
        ),
    ]
