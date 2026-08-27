from django.urls import path
from men import views
urlpatterns = [
    path('', views.men,name='men'),
]
