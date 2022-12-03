from django.urls import path
from . import views

urlpatterns = [
    path("traits/", views.TraitsView.as_view()),
]
