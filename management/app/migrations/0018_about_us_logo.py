# Generated by Django 4.2.1 on 2023-05-19 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_rename_about_us_image_about_us_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_us',
            name='logo',
            field=models.ImageField(null=True, upload_to='logo'),
        ),
    ]