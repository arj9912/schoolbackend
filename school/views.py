from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from school.models import Album, CarouselItem, Carousel, Faculty, Notice, Testimony
from school.serializers import AlbumSerializer, CarouselItemSerilaizer, CarouselSerilaizer, FacultySerializer, NoticeSerializer, TestimonySerializer
# Create your views here.


class CarouselViewSet(ModelViewSet):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerilaizer


class FacultyViewSet(ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class TestimonyViewSet(ModelViewSet):
    queryset = Testimony.objects.all()
    serializer_class = TestimonySerializer


class NoticeViewSet(ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
