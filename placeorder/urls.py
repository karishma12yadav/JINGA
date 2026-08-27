from django.urls import path
from placeorder import views

urlpatterns = [
    path('', views.placeorder )
]
