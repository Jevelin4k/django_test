
from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {''}
    return render(request, 'basic_app/index.html')

def other(request):
    return render(request, 'basic_app/other.html')

def url_page(request):
    return render(request, 'basic_app/url_page.html')