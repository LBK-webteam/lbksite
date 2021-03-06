# Generated by Django 2.2.6 on 2020-03-10 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_remove_vacancy_vacancy_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbmember',
            name='function',
            field=models.CharField(choices=[(1, 'Preses'), (2, 'Vice-preses'), (3, 'Penningmeester'), (4, 'Secretaris'), (5, 'Gnorgl verantwoordelijke'), (6, 'Gnorgl boekhouder'), (7, 'Baarr verantwoordelijke'), (8, 'Baarr boekhouder'), (9, 'Activiteiten verantwoordelijke'), (10, 'Sport verantwoordelijke'), (11, 'Cultuur verantwoordelijke'), (12, 'Internationaal verantwoordelijke'), (13, 'Bedrijvenrelaties verantwoordelijke'), (14, 'Bedrijvenrelaties vice-verantwoordelijke'), (15, 'Onderwijs verantwoordelijke'), (16, 'Onderwijs secretaris'), (17, 'Logistiek verantwoordelijke'), (18, 'Cursusdienst verantwoordelijke'), (19, 'ICT-verantwoordelijke')], max_length=50, primary_key=True, serialize=False, verbose_name='Functie'),
        ),
    ]
