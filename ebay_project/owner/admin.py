from django.contrib import admin
from owner.models import category,product,cart


# Register your models here.
admin.site.register(category)
admin.site.register(product)
admin.site.register(cart)