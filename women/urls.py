from django.urls import path
from women import views
urlpatterns = [
    path('',views.women,name='women'),
]
