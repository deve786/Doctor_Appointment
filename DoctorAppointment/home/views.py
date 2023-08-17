from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors
from .forms import BookingForm
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
    if request.method=="POST":
            form=BookingForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request,'confirmation.html')
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)

def contact(request):
    return render(request,'contact.html')

def department(request):
    dept_dict={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dept_dict)