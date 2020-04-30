from django.contrib import admin
from .models import Product, Contact, Banner,Order

# Register your models here.

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Banner)
admin.site.register(Order)