from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "main_app/home.html")

def contact_page(request):
    return render(request, "main_app/contact.html")

def aboutpage(request):
    return render(request, "main_app/about.html")