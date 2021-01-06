from django.urls import path
from . import views
from django.contrib.auth import login

app_name = 'users'
urlpatterns = [
    path('register/', views.registration, name='register'),
    path('register/tutor', views.tutor_registration, name='tutorregister'),
]
