# Generated by Django 3.2.6 on 2021-08-09 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_barbearia_date_closed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barbearia',
            name='closed_hour',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='barbearia',
            name='open_hour',
            field=models.TimeField(null=True),
        ),
    ]
