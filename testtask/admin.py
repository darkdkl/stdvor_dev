from django.contrib import admin
from .models import Product, Order, Сontact


class OrderInline(admin.TabularInline):
    model = Order
    extra = 0


admin.site.register(Product)


admin.site.register(Order)


@admin.register(Сontact)
class СontactsAdmin(admin.ModelAdmin):
    inlines = [OrderInline]
