# Generated by Django 2.2.1 on 2019-10-09 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_post_post_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='DBmember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='Voornaam')),
                ('last_name', models.CharField(max_length=200, verbose_name='Achternaam')),
                ('function', models.CharField(choices=[('Preses', 'Preses'), ('Vice-preses', 'Vice-preses'), ('Secretaris', 'Secretaris'), ('Gnorgl verantwoordelijke', 'Gnorgl verantwoordelijke'), ('Gnorgl boekhouder', 'Gnorgl boekhouder'), ('Baarr verantwoordelijke', 'Baarr verantwoordelijke'), ('Baarr boekhouder', 'Baarr boekhouder'), ('Activiteiten verantwoordelijke', 'Activiteiten verantwoordelijke'), ('Sport verantwoordelijke', 'Sport verantwoordelijke'), ('Cultuur verantwoordelijke', 'Cultuur verantwoordelijke'), ('Internationaal verantwoordelijke', 'Internationaal verantwoordelijke'), ('Bedrijvenrelaties verantwoordelijke', 'Bedrijvenrelaties verantwoordelijke'), ('Bedrijvenrelaties vice-verantwoordelijke', 'Bedrijvenrelaties vice-verantwoordelijke'), ('Onderwijs verantwoordelijke', 'Onderwijs verantwoordelijke'), ('Onderwijs secretaris', 'Onderwijs secretaris'), ('Logistiek verantwoordelijke', 'Logistiek verantwoordelijke'), ('Cursusdienst verantwoordelijke', 'Cursusdienst verantwoordelijke'), ('ICT verantwoordelijke', 'ICT-verantwoordelijke')], max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
    ]
