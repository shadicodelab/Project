from django.shortcuts import render, redirect
from .models import Appetizer, Entree, User, Cart
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

def remove_item(request):
    if request.method == "POST" and request.is_ajax():
        item_id = request.POST.get('item_id')

        if not item_id:
            return JsonResponse({'error': 'Item ID is missing'}, status=400)

        selected_items = request.session.get('selected_items', [])

        # Find the item with the given ID and remove it from the session
        for item in selected_items:
            if str(item.get('id')) == item_id:
                selected_items.remove(item)
                request.session['selected_items'] = selected_items
                
                # Calculate and return the total price
                total_price = sum(item['price'] for item in selected_items)
                return JsonResponse({'message': 'Item removed successfully', 'total_price': total_price})

        return JsonResponse({'error': 'Item not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=405)




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
        
        try:
            appetizer = Appetizer.objects.get(id=appetizer_id)
        except Appetizer.DoesNotExist:
            return HttpResponse("Invalid appetizer ID", status=400)

        user_cart, created = Cart.objects.get_or_create(user=request.user)
        user_cart.appetizers.add(appetizer)
        selected_items = request.session.get('selected_items', [])
        selected_items.append({
            'name': appetizer.name,
            'price': float(appetizer.price), 
        })
        request.session['selected_items'] = selected_items

        return redirect('appetizer')
    return render(request, 'food/index.html')

def customer_order(request):
    selected_items = request.session.get('selected_items', [])
    total_price = sum(item['price'] for item in selected_items)

    return render(request, 'food/order.html', {'selected_items': selected_items, 'total_price': total_price})





    