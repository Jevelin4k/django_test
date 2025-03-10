from django.urls import path
from base_app import views

app_name = 'base_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
]