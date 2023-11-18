from django.conf import settings
from django.db import models


class CarouselButton(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)


# Create your models here.


class Carousel(models.Model):
    id = models.BigAutoField(primary_key=True)


class CarouselItem(models.Model):
    carousel = models.ForeignKey(
        Carousel, on_delete=models.CASCADE, related_name='items'
    )
    heading = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='carousel/')
    primary_button_label = models.CharField(max_length=255, blank=True, null=True)
    primary_button_link = models.CharField(
        max_length=255, blank=True, null=True)
    secondary_button_label = models.CharField(
        max_length=255, blank=True, null=True)
    secondary_button_link = models.CharField(
        max_length=255, blank=True, null=True)
    

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='faculties/')
    description = models.TextField()


class Testimony(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField(max_length=10)


class Notice(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='notices/')
    uploaded_date = models.DateField(auto_now=True)


class Album(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='album/')


class AlbumImage(models.Model):
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name='images'
    )
    image = models.ImageField(upload_to='album/')


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='blog/thumbnails')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class UserReview(models.Model):
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='review/')
    review = models.CharField(max_length=200)
