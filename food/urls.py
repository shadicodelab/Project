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
    path('cart', views.cart, name='cart'),
    path('customer_order/', views.customer_order, name='customer_order'),
    path('remove_item/', views.remove_item, name='remove_item'),
]
