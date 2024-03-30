from django.contrib import admin
from .models import Appetizer,Entree, User, Cart

# Register your models here.
class appetizerAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    
class entreeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    
admin.site.register(Appetizer, appetizerAdmin)
admin.site.register(Entree, entreeAdmin)
admin.site.register(User)
admin.site.register(Cart)