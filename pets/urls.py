from django.urls import path
from . import views

urlpatterns = [
    path("pets/", views.PetsView.as_view()),
]
