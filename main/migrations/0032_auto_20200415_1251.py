# Generated by Django 2.2.6 on 2020-04-15 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20200412_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page_werkgroeplogo',
            field=models.ImageField(default='werkgroepen/sport.png', upload_to='werkgroepen', verbose_name='Icoon'),
        ),
    ]