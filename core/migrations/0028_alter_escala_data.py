# Generated by Django 3.2.5 on 2021-07-09 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_alter_folga_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escala',
            name='data',
            field=models.DateField(null=True),
        ),
    ]
