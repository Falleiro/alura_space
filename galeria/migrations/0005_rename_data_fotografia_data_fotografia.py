# Generated by Django 5.0 on 2023-12-28 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0004_fotografia_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fotografia',
            old_name='data',
            new_name='data_fotografia',
        ),
    ]
