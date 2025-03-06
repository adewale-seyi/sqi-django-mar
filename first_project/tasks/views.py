from django.shortcuts import render,HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse("This is the Homepage!")

def all_tasks(request):
    return HttpResponse("This is the all tasks page!")
