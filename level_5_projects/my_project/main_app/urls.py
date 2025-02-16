from django.urls import path
from main_app import views



app_name = 'main_app'

urlpatterns = [
    path('registration/', views.register, name='registration'),
    path('user_login/', views.user_login, name='user_login'),
]