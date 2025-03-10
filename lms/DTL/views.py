from django.shortcuts import render

# Create your views here.
def cartpage(request):
    context = {
        "user": "Sammy",
        "cart_items": ["tomato", "strawberry", "vanilla ice cream","burger","cake"],
        "is_favourite": True,
        "no_of_items_in_carts": 5,
    }
    
    return render(request, "cart/cart.html", context)