# Generated by Django 3.2.6 on 2021-08-18 13:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210818_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='ordem_servico',
        ),
        migrations.AddField(
            model_name='agenda',
            name='servico',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='api.servico'),
            preserve_default=False,
        ),
    ]
