# Generated by Django 2.2.1 on 2019-07-16 10:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ruyatabiri', '0002_auto_20190609_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruyatabiri',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
