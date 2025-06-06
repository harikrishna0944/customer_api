from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, RegisterView

router = DefaultRouter()
router.register('customers', CustomerViewSet, basename='customer')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
]

