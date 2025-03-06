from django.urls import path
from . import views
app_name = "template_practice"

urlpatterns = [
    path('', views.welcome, name='my_app'),
]