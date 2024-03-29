# Generated by Django 3.2.6 on 2021-08-05 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barbearia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('endereco', models.CharField(max_length=100)),
                ('avatar', models.URLField()),
                ('bio', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('document', models.CharField(max_length=50)),
                ('date_closed', models.DateField()),
                ('open_hour', models.TimeField()),
                ('closed_hour', models.TimeField()),
            ],
            options={
                'db_table': 'barbearia',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('avatar', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('avatar', models.URLField()),
                ('price', models.FloatField()),
                ('barbearia', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='api.barbearia')),
            ],
            options={
                'db_table': 'servico',
            },
        ),
        migrations.CreateModel(
            name='Ordem_Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('avaliacao', models.FloatField()),
                ('barbearia', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='api.barbearia')),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='api.cliente')),
                ('servico', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='api.servico')),
            ],
            options={
                'db_table': 'ordem_servico',
            },
        ),
    ]
