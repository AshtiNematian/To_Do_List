# Generated by Django 3.2.4 on 2021-07-31 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='slugs',
            new_name='slug',
        ),
    ]
