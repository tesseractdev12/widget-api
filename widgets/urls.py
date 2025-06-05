from rest_framework.routers import DefaultRouter
from .views import WidgetViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'', WidgetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
