# Generated by Django 4.2.7 on 2023-11-09 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_testimony'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimony',
            old_name='number',
            new_name='count',
        ),
    ]
