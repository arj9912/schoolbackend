
from school.models import Album, AlbumImage, Carousel, CarouselItem, Faculty, Notice, Testimony
from rest_framework import serializers


class CarouselItemSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = CarouselItem
        fields = ['id', 'heading', 'title', 'description', 'image', 'primary_button_label', 'primary_button_link', 'secondary_button_label', 'secondary_button_link']


class CarouselSerilaizer(serializers.ModelSerializer):
    items = CarouselItemSerilaizer(many=True)
    class Meta:
        model = Carousel
        fields = ['id', 'items']


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id', 'name', 'image', 'description']


class TestimonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimony
        fields = ['id', 'name', 'count']


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['id', 'title', 'description', 'image', 'uploaded_date']


class AlbumImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumImage
        fields = ['id', 'image']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'description', 'thumbnail']
