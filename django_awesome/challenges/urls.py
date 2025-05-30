from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("february", views.february),
    path("march", views.march),
    path("<int:month>", views.monthly_challenges_by_number),
    path("<str:month>", views.monthly_challenges, name="monthly-challenge")
]