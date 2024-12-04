# Generated by Django 4.2.16 on 2024-12-04 08:19

from django.db import migrations, models
import employer_profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('employer_profiles', '0002_employerprofile_industry'),
    ]

    operations = [
        migrations.AddField(
            model_name='employerprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=employer_profiles.models.upload_to),
        ),
        migrations.AlterField(
            model_name='employerprofile',
            name='company_description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='employerprofile',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employerprofile',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
