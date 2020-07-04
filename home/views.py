from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.template import loader


@login_required(login_url='/accounts/login')
def home(request):
    template = loader.get_template('home/index.html')
    return render(request, 'home/index.html')
