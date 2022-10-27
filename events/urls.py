from django.urls import path, include
from .views import event_main

urlpatterns = [
    path('', event_main, name="event_main"),
]