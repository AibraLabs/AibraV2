# Generated by Django 4.1.3 on 2022-12-16 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_job_skill_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='skill_tag',
        ),
    ]
