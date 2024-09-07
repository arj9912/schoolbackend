from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from school.models import AboutUs, Album, CarouselItem, Carousel, ContactUs, Courses, Faculty, Milestones, Notice, OnlineAdministration, PopUp, Suggestion, Team, Testimonial
from school.serializers import (
    AboutUsSerializer,
    AlbumSerializer,
    CarouselItemSerilaizer,
    CarouselSerilaizer,
    ContactUsSerializer,
    CourseSerializer,
    FacultySerializer,
    NoticeSerializer,
    MilestonesSerializer,
    OnlineAdministrationSerializer,
    PopUpSerializer,
    SuggestionSerializer,
    TeamSerializer,
    TestimonialSerializer,
)

# Create your views here.


class CarouselViewSet(ModelViewSet):
    queryset = Carousel.objects.all() 
    serializer_class = CarouselSerilaizer


class FacultyViewSet(ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class MilestonesViewSet(ModelViewSet):
    queryset = Milestones.objects.all()
    serializer_class = MilestonesSerializer


class NoticeViewSet(ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class ContactUsViewSet(ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

class PopUpViewSet(ModelViewSet):
    queryset = PopUp.objects.all()
    serializer_class = PopUpSerializer

class AboutUsViewSet(ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class CoursesViewSet(ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer

class TestimonialViewSet(ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    

class SuggestionViewSet(ModelViewSet):
    queryset = Suggestion.objects.all()
    serializer_class = SuggestionSerializer

class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class OnlineAdministrationViewSet(ModelViewSet):
    queryset = OnlineAdministration.objects.all()
    serializer_class = OnlineAdministrationSerializer