# Generated by Django 2.1.4 on 2019-02-23 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0006_remove_profile_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
