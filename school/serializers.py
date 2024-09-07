from school.models import (
    Album,
    AlbumImage,
    Carousel,
    CarouselItem,
    Faculty,
    Notice,
    ContactUs,
    OnlineAdministration,
    PopUp,
    AboutUs,
    Courses,
    Team,
    Testimonial,
    Milestones,
    Suggestion
)
from rest_framework import serializers


class CarouselItemSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = CarouselItem
        fields = [
            "id",
            "heading",
            "title",
            "description",
            "image",
            "primary_button_label",
            "primary_button_link",
            "secondary_button_label",
            "secondary_button_link",
        ]


class CarouselSerilaizer(serializers.ModelSerializer):
    items = CarouselItemSerilaizer(many=True)

    class Meta:
        model = Carousel
        fields = ["id", "items"]


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ["id", "name", "image", "description"]


class MilestonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestones
        fields = ["id", "name", "count"]


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ["id", "title", "description", "image", "uploaded_date"]


class AlbumImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumImage
        fields = ["id", "image"]


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["id", "title", "description", "thumbnail"]


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ["id", "full_name", "email", "phone_no", "description"]

class PopUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopUp
        fields = ["id", "name", "image"]

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ["id", "heading", "title", "description", "author", "image"]

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ["id", "name", "image", "description"]


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ["id", "name", "image", "description", "position"]


class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = ["id", "name", "email", "phone_no", "description"]

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "title", "name", "position", "qualification", "year_of_experience", "image", "is_management", "is_administrative", "is_staff"]


class OnlineAdministrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineAdministration
        fields = ["id", "link"]