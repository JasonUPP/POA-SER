# Generated by Django 2.2 on 2019-04-24 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anteproyecto', '0022_antepi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antepi',
            name='imagen',
            field=models.ImageField(upload_to='apimg'),
        ),
    ]
