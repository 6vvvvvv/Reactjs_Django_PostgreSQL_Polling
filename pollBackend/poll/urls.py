from django.urls import path
from . import views


urlpatterns = [
    path('polling/', views.polling),
    path('initial/', views.initial),
]
