# Generated by Django 3.2.5 on 2021-07-08 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210708_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cad_folga_semanal',
            name='disponivel',
        ),
        migrations.AddField(
            model_name='cad_manual_escalas',
            name='disponivel',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
