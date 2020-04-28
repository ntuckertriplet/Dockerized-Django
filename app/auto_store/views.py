from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import EmployeeCreationForm

# Create your views here.


def index_view(request):
    return render(request, 'index.html')
