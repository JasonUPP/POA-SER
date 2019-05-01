# Generated by Django 2.1.4 on 2019-02-23 05:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anteproyecto', '0014_remove_anteproyecto_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='anteproyecto',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]