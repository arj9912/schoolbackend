# Generated by Django 4.2.7 on 2023-11-09 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carouselitem',
            name='primary_button',
        ),
        migrations.RemoveField(
            model_name='carouselitem',
            name='secondary_button',
        ),
        migrations.AddField(
            model_name='carouselitem',
            name='primary_button_label',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='carouselitem',
            name='primary_button_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='carouselitem',
            name='secondary_button_label',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='carouselitem',
            name='secondary_button_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
