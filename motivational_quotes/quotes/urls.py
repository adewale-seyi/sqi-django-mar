from django.urls import path
from . import views

app_name = "Motivational_quotes"

urlpatterns = [
    path('quotes/', views.get_quotes, name='quotes'),
]