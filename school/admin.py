from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget

from school.models import AboutUs, Album, AlbumImage, Blog, Carousel, CarouselItem, ContactUs, Courses, Faculty, Milestones, OnlineAdministration, PopUp, Suggestion, Team, Testimonial


class CarouselItemAdminInline(admin.StackedInline):
    model = CarouselItem
    extra = 1


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = [CarouselItemAdminInline]


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class AlbumImageAdmin(admin.StackedInline):
    model = AlbumImage
    min_num = 1
    extra = 1


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', "description"]
    inlines = [AlbumImageAdmin]


@admin.register(Milestones)
class MilestonesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', "count"]


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', "email", "phone_no", "description"]


@admin.register(PopUp)
class PopUpAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', "image"]

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'heading', "title", "description", "author", "image"]

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', "image", "description"]

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', "image", "description", "position"]


@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', "email", "phone_no", "description"]

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', "name", "position", "qualification", "year_of_experience", "image", "is_management", "is_administrative", "is_staff"]

@admin.register(OnlineAdministration)
class OnlineAdministrationAdmin(admin.ModelAdmin):
    list_display = ['id', 'link']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', "author","thumbnail", "created_at", "updated_at"]