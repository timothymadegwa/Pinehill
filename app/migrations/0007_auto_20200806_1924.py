# Generated by Django 3.0.8 on 2020-08-06 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_job_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('cover', models.FileField(upload_to='jobs/covers')),
                ('cv', models.FileField(upload_to='jobs/cv')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Job')),
            ],
        ),
    ]
