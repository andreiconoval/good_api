from django.urls import path

from . import views

urlpatterns = [
    path('<str:q>/', views.index, name='index'),
    path('load', views.load_city_json, name='load'),
]