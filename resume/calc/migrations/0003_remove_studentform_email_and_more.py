# Generated by Django 5.0.1 on 2024-01-29 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_alter_studentform_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentform',
            name='email',
        ),
        migrations.RemoveField(
            model_name='studentform',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='studentform',
            name='lastname',
        ),
    ]
