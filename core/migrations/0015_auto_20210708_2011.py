# Generated by Django 3.2.5 on 2021-07-08 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_cad_medico_disponivel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cad_folga_semanal',
            name='dia_da_semana',
        ),
        migrations.AddField(
            model_name='cad_folga_semanal',
            name='medico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.cad_medico'),
        ),
    ]