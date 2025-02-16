from django.urls import path
from basic_app import views

# TEMPLATES TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('url_page/', views.url_page, name='url_page'),
    path('other/', views.other, name='other'),
]