# Generated by Django 3.2.6 on 2021-08-12 21:43

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210809_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordem_servico',
            name='comentario',
            field=django_quill.fields.QuillField(default=str(0)),
            preserve_default=False,
        ),
    ]