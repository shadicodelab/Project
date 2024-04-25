from django.shortcuts import get_object_or_404, render, redirect
from .models import Appetizer, Entree, User, Cart
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
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
    
    # Get the user's cart or create a new one if it doesn't exist
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    
    Appetizers = Appetizer.objects.all()
    ctx = {'appetizers': Appetizers, 'active_link': 'appetizer', 'cart': user_cart}
    
    return render(request, 'food/appetizer.html', ctx)


@csrf_exempt
def order(request):
    request.session.set_expiry(0)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.method == 'POST':
            note = request.POST.get('note')
            orders = request.POST.get('orders')
            request.session['note'] = note
            request.session['orders'] = orders
            print(note)
            print(orders)
            # Assuming you want to return some JSON response
            return JsonResponse({'success': True})
    ctx = {'active_link':'order'}
    return render(request,'food/order.html', ctx)

def success(request):
    orders = request.session['orders']
    ctx = {'orders':orders}
    return render(request, 'food/success.html', ctx)

def entree(request):
    # Get the user's cart or create a new one if it doesn't exist
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    
    entree = Entree.objects.all()
    ctx = {'entrees': entree, 'active_link': 'entree', 'cart': user_cart}
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
    
    
def cart(request):
    if request.method == "POST":
        appetizer_id = request.POST.get('appetizer_id')
        appetizer = Appetizer.objects.get(id=appetizer_id)

        user_cart, created = Cart.objects.get_or_create(user=request.user)

        user_cart.appetizers.add(appetizer)

        return redirect('appetizer') 

    return render(request, 'food/index.html')

def entree_cart(request):
    if request.method == "POST":
        entree_id = request.POST.get('entree_id') or request.POST.get('entree_id')
        entree = Entree.objects.get(id=entree_id)

        user_cart, created = Cart.objects.get_or_create(user=request.user)

        user_cart.entrees.add(entree)

        return redirect('entree') 

    return render(request, 'food/index.html')

from django.db.models import Count

def order(request):
    if request.method == "POST":
        cart_id = request.POST.get('cart_id')
        user_cart = get_object_or_404(Cart, id=cart_id)
        cart_items = user_cart.appetizers.all()
        entree_items = user_cart.entrees.all()

    
        cart_items = user_cart.appetizers.annotate(count=Count('id'))

        # Annotate each entree with its count in the cart
        entree_items = user_cart.entrees.annotate(count=Count('id'))

        return render(request, 'food/order.html', {
            'cart_items': cart_items,
            'entree_items': entree_items,
        })
    else:
        # Handle GET request (if any specific logic needed)
        return redirect('appetizer')


def checkout(request):
    if request.method == "POST":
        cart_id = request.POST.get('cart_id')
        user_cart = get_object_or_404(Cart, id=cart_id)
        feedback = request.POST.get("feedback")

        # Reduce stock quantity for appetizers
        for cart_item in user_cart.appetizers.all():
            appetizer = cart_item.appetizer
            appetizer.stock -= cart_item.quantity
            appetizer.save()

        # Reduce stock quantity for entrees
        for entree_cart_item in user_cart.entrees.all():
            entree = entree_cart_item.entree
            entree.stock -= entree_cart_item.quantity
            entree.save()

        # Clear the cart after checkout
        user_cart.appetizers.clear()
        user_cart.entrees.clear()

        # Process the feedback (e.g., save it to the database)
        if feedback:
            # Process the feedback here

            return redirect('success')

    return render(request, 'checkout.html')