# Generated by Django 3.2.5 on 2021-07-08 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_cad_folga_semanal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cad_manual_escalas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.cad_folga_semanal')),
                ('medico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.cad_medico')),
                ('posto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.cad_posto')),
            ],
        ),
    ]