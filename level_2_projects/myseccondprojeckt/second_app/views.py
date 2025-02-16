from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'warning_page': 'WARNING!'}
    return render(request, 'second_app/users.html', context=my_dict)