from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = forms.ForName()

    if request.method == 'POST':
        form = forms.ForName(request.POST)

        if form.is_valid():
            print('VALIDATION SECCESS!')
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])



    return render(request, 'basicapp/form_page.html', {'form': form})