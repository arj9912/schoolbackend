# Generated by Django 4.2.7 on 2023-11-09 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_remove_carouselitem_primary_button_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='faculties/')),
                ('description', models.TextField()),
            ],
        ),
    ]
