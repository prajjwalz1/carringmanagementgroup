# Generated by Django 4.1.6 on 2023-05-16 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='id',
        ),
        migrations.AddField(
            model_name='appointment',
            name='email',
            field=models.EmailField(default='test@gmail.com', max_length=254, primary_key=True, serialize=False),
        ),
    ]
