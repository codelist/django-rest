from django.conf.urls import url, include
from rest_framework import routers
from .views import NoticeViewSet


router = routers.DefaultRouter()
router.register(r'notices', NoticeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
