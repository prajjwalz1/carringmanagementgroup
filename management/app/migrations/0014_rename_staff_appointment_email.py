# Generated by Django 4.1.6 on 2023-05-16 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_appointment_email_appointment_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='staff',
            new_name='email',
        ),
    ]
