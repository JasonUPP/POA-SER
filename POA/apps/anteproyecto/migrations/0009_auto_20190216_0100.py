# Generated by Django 2.1.4 on 2019-02-16 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anteproyecto', '0008_auto_20190216_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anteproyecto',
            name='fila',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='anteproyecto',
            name='total',
            field=models.FloatField(blank=True, max_length=30, null=True),
        ),
    ]