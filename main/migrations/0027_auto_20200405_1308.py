# Generated by Django 2.2.6 on 2020-04-05 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20200405_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='running',
            name='members_c',
            field=models.TextField(blank=True, null=True, verbose_name='Leden van de lolploeg'),
        ),
        migrations.AddField(
            model_name='running',
            name='motivation_b',
            field=models.TextField(blank=True, null=True, verbose_name='Motivatie (B)'),
        ),
    ]
