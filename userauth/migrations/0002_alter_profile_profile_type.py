# Generated by Django 4.0.4 on 2022-05-20 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_type',
            field=models.CharField(choices=[('officer', 'officer'), ('pastoralist', 'pastoralist')], max_length=100),
        ),
    ]