# Generated by Django 4.2.1 on 2023-05-15 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_about_us_slide'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_us',
            name='Company_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='about_us',
            name='Title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='about_us',
            name='Total_projects',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='about_us',
            name='description',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='about_us',
            name='years_of_experience',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
