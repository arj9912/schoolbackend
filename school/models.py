from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField

class CarouselButton(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)


# Create your models here.


class Carousel(models.Model):
    id = models.BigAutoField(primary_key=True)


class CarouselItem(models.Model):
    carousel = models.ForeignKey(
        Carousel, on_delete=models.CASCADE, related_name="items"
    )
    heading = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="carousel/")
    primary_button_label = models.CharField(max_length=255, blank=True, null=True)
    primary_button_link = models.CharField(max_length=255, blank=True, null=True)
    secondary_button_label = models.CharField(max_length=255, blank=True, null=True)
    secondary_button_link = models.CharField(max_length=255, blank=True, null=True)


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="faculties/")
    description = models.TextField()


class Milestones(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField()


class Notice(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="notices/")
    uploaded_date = models.DateField(auto_now=True)


class Album(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="album/")


class AlbumImage(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="album/")


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    thumbnail = models.ImageField(upload_to="blog/thumbnails")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class UserReview(models.Model):
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="review/")
    review = models.CharField(max_length=200)

class ContactUs(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone_no = models.CharField(max_length=15)
    description = models.CharField(max_length=255)

class PopUp(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="pop_up/")

class AboutUs(models.Model):
    heading = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to="about_us/")

class Courses(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="courses/")
    description = models.CharField(max_length=255)


class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="testimonials/")
    description = models.CharField(max_length=255)
    position = models.CharField(max_length=255)


class Suggestion(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    description = models.CharField(max_length=255)

class Team(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    year_of_experience = models.CharField(max_length=255)
    image = models.ImageField(upload_to="team/")
    is_management = models.BooleanField(default=False)
    is_administrative = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    

class OnlineAdministration(models.Model):
    link = models.URLField()