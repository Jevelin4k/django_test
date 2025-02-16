from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import User
# Create your views here.

def index(request):
    return render(request, 'main_app/index.html')

def users(request):
    userName_list = User.objects.order_by('email')
    userName_dict = {'User': userName_list}
    return render(request, 'main_app/users.html', context=userName_dict)