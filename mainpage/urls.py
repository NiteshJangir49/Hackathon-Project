from django.urls import path
from mainpage import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]