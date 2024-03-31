from django.shortcuts import render, redirect
from .models import Appetizer, Entree, User, Cart
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request,'food/index.html')


def appetizer(request):
    Appetizers = Appetizer.objects.all()
    return render(request,'food/appetizer.html', {'appetizers':Appetizers})


def order(request):
    return render(request,'food/order.html')

def entree(request):
    entrees = Entree.objects.all()
    return render(request,'food/entree.html', {'entrees':entrees})

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("appetizer"))
        else:
            return render(request, "food/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "food/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "food/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "food/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "food/register.html")


def cart(request):
    if request.method == "POST":
        appetizer_id = request.POST.get('appetizer_id')
        appetizer = Appetizer.objects.get(id=appetizer_id)

        # Get or create cart for the current user
        user_cart, created = Cart.objects.get_or_create(user=request.user)

        # Add the selected appetizer to the cart
        user_cart.appetizers.add(appetizer)

        # Redirect back to the appetizer page after adding to cart
        return redirect('appetizer')

    # Render the index.html template if the request method is not POST
    return render(request, 'food/index.html')
        
