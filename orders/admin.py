from django.contrib import admin


from orders.models import Order

@admin.register(Order)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('client', 'product', 'payment_method')