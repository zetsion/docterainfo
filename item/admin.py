from django.contrib import admin
from .models import ItemCategory, Item, Rating

admin.site.register(ItemCategory)
admin.site.register(Item)
admin.site.register(Rating)

# Register your models here.
