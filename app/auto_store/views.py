from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import EmployeeCreationForm

# Create your views here.


def index_view(request):
    return render(request, 'index.html')


def products(request):
    return render(request, 'products.html')


def services(request):
    return render(request, 'services.html')


@login_required(login_url='/')
def employees(request):
    return render(request, 'employee.html')


def customer_memo(request):
    return render(request, 'customerMemo.html')


def employee_holiday(request):
    return render(request, 'employeeHoliday.html')


def shutdown(request):
    return render(request, 'shutdown.html')


def w2(request):
    return render(request, 'w2.html')


def ceo_message(request):
    return render(request, 'ceoMessage.html')


def covid19(request):
    return render(request, 'covid19.html')


def testing(request):
    return render(request, 'testing.html')


def bulletin(request):
    return render(request, 'bulletin.html')


@login_required(login_url='/')
def add_user(request):
    if request.method == 'POST':
        f = EmployeeCreationForm(request.POST, initial={})
        if f.is_valid():
            f.save()
            return redirect('employees')

    else:
        f = EmployeeCreationForm()
        return render(request, 'adduser.html', {'form': f})


def help(request):
    return render(request, 'help.html')
