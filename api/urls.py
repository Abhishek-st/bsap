from django.urls import path
from . import views

urlpatterns = [
    path('countries/', views.Countries.as_view()),
    path('countries/<str:pk>/', views.CountriesFilter.as_view()),
]