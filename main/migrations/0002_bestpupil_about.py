# Generated by Django 4.1.1 on 2022-09-24 15:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bestpupil',
            name='about',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
