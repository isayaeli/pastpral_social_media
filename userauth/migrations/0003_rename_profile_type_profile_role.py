# Generated by Django 4.0.4 on 2022-05-20 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_alter_profile_profile_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_type',
            new_name='role',
        ),
    ]
