# Generated by Django 2.2.1 on 2019-10-09 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20191009_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dbmember',
            name='id',
        ),
        migrations.AlterField(
            model_name='dbmember',
            name='function',
            field=models.CharField(choices=[('Preses', 'Preses'), ('Vice-preses', 'Vice-preses'), ('Secretaris', 'Secretaris'), ('Gnorgl verantwoordelijke', 'Gnorgl verantwoordelijke'), ('Gnorgl boekhouder', 'Gnorgl boekhouder'), ('Baarr verantwoordelijke', 'Baarr verantwoordelijke'), ('Baarr boekhouder', 'Baarr boekhouder'), ('Activiteiten verantwoordelijke', 'Activiteiten verantwoordelijke'), ('Sport verantwoordelijke', 'Sport verantwoordelijke'), ('Cultuur verantwoordelijke', 'Cultuur verantwoordelijke'), ('Internationaal verantwoordelijke', 'Internationaal verantwoordelijke'), ('Bedrijvenrelaties verantwoordelijke', 'Bedrijvenrelaties verantwoordelijke'), ('Bedrijvenrelaties vice-verantwoordelijke', 'Bedrijvenrelaties vice-verantwoordelijke'), ('Onderwijs verantwoordelijke', 'Onderwijs verantwoordelijke'), ('Onderwijs secretaris', 'Onderwijs secretaris'), ('Logistiek verantwoordelijke', 'Logistiek verantwoordelijke'), ('Cursusdienst verantwoordelijke', 'Cursusdienst verantwoordelijke'), ('ICT verantwoordelijke', 'ICT-verantwoordelijke')], max_length=50, primary_key=True, serialize=False),
        ),
    ]
