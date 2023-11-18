
from rest_framework_nested import routers

from . import views


router = routers.DefaultRouter()

router.register('carousels', views.CarouselViewSet)
router.register('faculties', views.FacultyViewSet)
router.register('testimonies', views.TestimonyViewSet)
router.register('notices', views.NoticeViewSet)
router.register('faculties', views.FacultyViewSet)
router.register('albums', views.AlbumViewSet)

urlpatterns = router.urls
