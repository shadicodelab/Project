from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('appetizer', views.appetizer, name = 'appetizer'),
    path('entree', views.entree, name = 'entree'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('order', views.order, name = 'order'),
    path('success', views.success, name = 'success'),
    path('cart', views.cart, name='cart'),
    path('order', views.order, name='order'),
    path('entreeCart', views.entree_cart, name='entreeCart'),
    path('checkout',views.checkout, name='checkout')
]
