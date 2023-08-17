from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors
# Create your views here.
def index(request):
    
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
def doctor(request):
    docs={
        'doc':Doctors.objects.all()
    }
    return render(request,'doctor.html',docs)

    
def booking(request):
    return render(request,'booking.html')

def contact(request):
    return render(request,'contact.html')

def department(request):
    dept_dict={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dept_dict)