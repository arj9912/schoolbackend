# Generated by Django 4.2.7 on 2023-11-08 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CarouselButton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CarouselItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='carousel/')),
                ('carousel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='school.carousel')),
                ('primary_button', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_button', to='school.carouselbutton')),
                ('secondary_button', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secondary_button', to='school.carouselbutton')),
            ],
        ),
    ]
