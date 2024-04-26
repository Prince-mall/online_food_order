from django.contrib import admin
from .models import Users,Restaurants,MenuCategories,MenuItems,Reviews,CartItem

admin.site.register(Users)
admin.site.register(Restaurants)
admin.site.register(MenuItems)
admin.site.register(MenuCategories)
admin.site.register(Reviews)
admin.site.register(CartItem)
