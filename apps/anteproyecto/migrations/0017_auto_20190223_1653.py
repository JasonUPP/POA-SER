# Generated by Django 2.1.4 on 2019-02-23 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anteproyecto', '0016_auto_20190223_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fila',
            name='anteProyecto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='anteproyecto.AnteProyecto'),
        ),
    ]
