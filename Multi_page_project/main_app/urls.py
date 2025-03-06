from django.urls import path
from . import views
app_name = "main_app"
urlpatterns = [
    path('home/', views.homepage, name='homepage'),
    path('contact-us/', views.contact_page, name='contact_page'),
    path('about-us/', views.aboutpage, name='about_us'),
] 