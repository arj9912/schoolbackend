# Generated by Django 4.2.7 on 2023-11-09 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_rename_number_testimony_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='notices/')),
                ('uploaded_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
