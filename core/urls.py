
from rest_framework_nested import routers

from . import views


router = routers.DefaultRouter()

# router.register('user', views)

urlpatterns = router.urls
