# Generated by Django 2.1.4 on 2019-02-23 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anteproyecto', '0015_anteproyecto_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fila',
            name='anteProyecto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fta', to='anteproyecto.AnteProyecto'),
        ),
    ]