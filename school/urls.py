
from rest_framework_nested import routers

from . import views


router = routers.DefaultRouter()

router.register('carousels', views.CarouselViewSet)
router.register('faculties', views.FacultyViewSet)
router.register('testimonials', views.TestimonialViewSet)
router.register('notices', views.NoticeViewSet)
router.register('faculties', views.FacultyViewSet)
router.register('albums', views.AlbumViewSet)
router.register('contactus',views.ContactUsViewSet)
router.register('popup', views.PopUpViewSet)
router.register('aboutus', views.AboutUsViewSet)
router.register('courses', views.CoursesViewSet)
router.register('milestones', views.MilestonesViewSet)
router.register('suggestions', views.SuggestionViewSet)
router.register('teams', views.TeamViewSet)
router.register('onlineadministrations', views.OnlineAdministrationViewSet)
urlpatterns = router.urls
