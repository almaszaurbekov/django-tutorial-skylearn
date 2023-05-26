from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<int:id>', views.room, name="room"),
    path('create-topic', views.create_topic, name="create_topic"),
    path('error', views.error, name="error"),
]