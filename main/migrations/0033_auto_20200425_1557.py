# Generated by Django 2.2.6 on 2020-04-25 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20200415_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='running',
            name='workgroup',
            field=models.CharField(blank=True, choices=[('Penning', 'Penning'), ('Communicatie', 'Communicatie'), ('Gnorgl', 'Gnorgl'), ('Baarr', 'Baarr'), ('Activiteiten', 'Activiteiten'), ('Sport', 'Sport'), ('Cultuur', 'Cultuur'), ('Internationaal', 'Internationaal'), ('Bedrijvenrelaties', 'Bedrijvenrelaties'), ('Onderwijs', 'Onderwijs'), ('Logistiek', 'Logistiek'), ('Cursusdienst', 'Cursusdienst'), ('ICT', 'ICT'), ('Onthaal', 'Onthaal'), ('Revue', 'Revue'), ('IFR', 'IFR'), ('Galabal', 'Galabal'), ('IAAS', 'IAAS'), ('Bloedserieus', 'Bloedserieus')], max_length=50, null=True, verbose_name='Werkgroep'),
        ),
    ]
