# Generated by Django 4.0.2 on 2022-02-07 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_domicilio_persona_domicilio'),
    ]

    operations = [
        migrations.AddField(
            model_name='domicilio',
            name='nro_calle',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]