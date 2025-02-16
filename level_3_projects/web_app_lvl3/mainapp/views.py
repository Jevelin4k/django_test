from django.shortcuts import render
from . import forms
from .models import User

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')

def sing_up(request):
    form = forms.User()

    if request.method == 'POST':
        form = forms.User(request.POST)

        if form.is_valid():
            users = User.objects.get_or_create(user_name=form.cleaned_data['User'], user_email=form.cleaned_data['Email'], user_password=form.cleaned_data['Password'])[0]
            users.save()
            return render(request, 'mainapp/index.html')

    return render(request, 'mainapp/sing_up.html', {'form':form})