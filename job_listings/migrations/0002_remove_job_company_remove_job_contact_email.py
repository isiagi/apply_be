# Generated by Django 4.2.16 on 2024-12-31 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_listings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='company',
        ),
        migrations.RemoveField(
            model_name='job',
            name='contact_email',
        ),
    ]
