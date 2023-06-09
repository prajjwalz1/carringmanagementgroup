# Generated by Django 4.2.1 on 2023-05-18 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_about_us_image_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about_us',
            old_name='About_us_image',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='blog',
            name='Publisher_image',
            field=models.ImageField(null=True, upload_to='projects'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='projects'),
        ),
        migrations.AlterField(
            model_name='our_team',
            name='image',
            field=models.ImageField(upload_to='projects'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(upload_to='carousel_images'),
        ),
        migrations.AlterField(
            model_name='testimony',
            name='image',
            field=models.ImageField(upload_to='projects'),
        ),
    ]
