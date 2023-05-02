from django.contrib import admin
from . models import Product
# from.models import Customer, Payment, Product, Order, Delivery

# admin.site.register(Customer)
# admin.site.register(Payment)
# admin.site.register(Product)
# admin.site.register(Order)
# admin.site.register(Delivery)
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discounted_price','category','product_image']