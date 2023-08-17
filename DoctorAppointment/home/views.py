from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    number={
        'num1':[0,1,2,3,4,5,6,7,8,9]
    }
    return render(request,'index.html',number)

def about(request):
    return render(request,'about.html')
def doctor(request):
    return render(request,'doctor.html')

    
def booking(request):
    return render(request,'booking.html')

def contact(request):
    return render(request,'contact.html')

def department(request):
    return render(request,'department.html')