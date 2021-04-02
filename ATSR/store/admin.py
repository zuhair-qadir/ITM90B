from django.contrib import admin
from .models import *

admin.site.register(Company)
admin.site.register(Tool)
admin.site.register(RentalOrder)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
