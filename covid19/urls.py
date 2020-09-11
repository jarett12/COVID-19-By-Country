from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Tracker-home'),
    path('charts/',views.charts, name='Tracker-charts')

]