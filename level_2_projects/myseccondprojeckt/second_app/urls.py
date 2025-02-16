from second_app import views
from django.urls import path

urlpatterns = [
    path('help', views.index, name='help')
]