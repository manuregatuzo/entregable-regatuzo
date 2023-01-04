from django.contrib import admin

from products.models import Products

#admin.site.register(Products)

@admin.register(Products)
class ProductAdminn(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')