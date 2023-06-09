# Generated by Django 4.2.1 on 2023-05-15 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='about_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('years_of_experience', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('Total_projects', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='carousel_images/')),
            ],
        ),
    ]
