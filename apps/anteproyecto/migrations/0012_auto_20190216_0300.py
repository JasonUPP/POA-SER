# Generated by Django 2.1.4 on 2019-02-16 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anteproyecto', '0011_auto_20190216_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fila',
            name='capitulo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='anteproyecto.Capitulo'),
        ),
        migrations.AlterField(
            model_name='fila',
            name='concepto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='anteproyecto.Concepto'),
        ),
        migrations.AlterField(
            model_name='fila',
            name='partidaespecifica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='anteproyecto.PartidaEspecifica'),
        ),
        migrations.AlterField(
            model_name='fila',
            name='partidagenerica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='anteproyecto.PartidaGenerica'),
        ),
    ]
