from django.urls import path
from . import views

urlpatterns = [
    path("pets/", views.PetsView.as_view()),
    path("pets/<pet_id>/", views.PetsDetailViewView.as_view()),
]
