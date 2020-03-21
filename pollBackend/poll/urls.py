from django.urls import path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'Pollingoption', views.Polloptiondata)
router.register(r'Pollingtitle', views.Polltitledata)

urlpatterns = [
    path('option/', views.Polloptiondata.as_view()),
    path('title/', views.Polltitledata.as_view()),
]