from django.shortcuts import render, redirect
from .models import Appetizer, Entree, User, Cart
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    request.session.set_expiry(0)
    ctx = {'active_link':'index'}
    return render(request,'food/index.html',ctx)


def appetizer(request):
    request.session.set_expiry(0)
    Appetizers = Appetizer.objects.all()
    ctx = {'appetizers':Appetizers, 'active_link':'appetizer'}
    return render(request,'food/appetizer.html', ctx)

@csrf_exempt
def order(request):
    request.session.set_expiry(0)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.method == 'POST':
            request.session['note'] = request.POST.get('note')
            print(request.session['note'])
            request.session['orders'] = request.POST.get('orders')
            print(request.session['orders'])
    ctx = {'active_link':'order'}
    return render(request,'food/order.html', ctx)

def success(request):
    orders = request.session['orders']
    ctx = {'orders':orders}
    return render(request, 'food/success.html', ctx)

def entree(request):
    entrees = Entree.objects.all()
    ctx = {'entrees':entrees, 'active_link':'entree'}
    return render(request,'food/entree.html', ctx)

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







    