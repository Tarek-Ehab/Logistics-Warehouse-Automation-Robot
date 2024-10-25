from django.contrib import admin
from .models import Classification,Zone,Supplier,Buyer ,Season,CarDrop,Shelf, Product,Order
# Register your models here.
 
admin.site.register(Classification)
admin.site.register(Supplier)
admin.site.register(Buyer)
admin.site.register(Zone)
admin.site.register(Season)
admin.site.register(CarDrop)
admin.site.register(Shelf)
admin.site.register(Product)
admin.site.register(Order)
# admin.site.register(Delivery)
