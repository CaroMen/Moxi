from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('signup/', views.signup),
    path('calendar/', views.cal),

]
