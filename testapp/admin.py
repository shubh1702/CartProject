from django.contrib import admin
from testapp.models import Cart,Product
# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ['name','quantity','price']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name']

admin.site.register(Cart,CartAdmin)
admin.site.register(Product,ProductAdmin)
