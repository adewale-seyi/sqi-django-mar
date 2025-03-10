from django.urls import path

from . import views

app_name = "DTL"

urlpatterns = [
    path("", views.cartpage, name="cart")
]