from django.contrib import admin

from school.models import Album, AlbumImage, Carousel, CarouselItem, Faculty, Testimony


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


@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', "count"]
