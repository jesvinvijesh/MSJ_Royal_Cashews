from django.contrib import admin
from django.contrib.auth.admin import User
from django.contrib.auth.admin import Group
from .models import *


# Register your models here.
class ExpenseAdmin(admin.ModelAdmin):
    # autocomplete_fields = ['agent_name', ]
    list_display = ['expense_category', 'amount', 'paid_on', 'agent_name']
    search_fields = ['amount', 'paid_on', ]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class deliveryAdmin(admin.ModelAdmin):
    list_display = ['agent_name', 'agent_address', 'contact_number']
    search_fields = ['agent_name', 'contact_number']

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class addressAdmin(admin.ModelAdmin):
    list_display = ['name', '__str__']
    search_fields = ['name', ]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class dealerAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_number', 'address']
    list_filter = ['address__city', ]
    search_fields = ['name', 'contact_number']

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class productAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'unit']
    search_fields = ['product_name', 'price', 'unit', ]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class paymentAdmin(admin.ModelAdmin):
    list_display = ['name', 'payment_type', 'date', 'status']
    search_fields = ['amount_paid', 'pending_amount']
    list_filter = ['date', ]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class oAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product', 'quantity', 'unit', 'amount', 'order_date']
    list_filter = ('product',)
    # autocomplete_fields = ['product']
    search_fields = ['customer', 'quantity', 'unit', 'amount', 'order_date']

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class customerAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'contact_number']
    search_fields = ['name', 'contact_number']

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


admin.site.register(expense, ExpenseAdmin)
admin.site.register(dealer, dealerAdmin)
admin.site.register(delivery_agent, deliveryAdmin)
admin.site.register(product, productAdmin)
admin.site.register(payment, paymentAdmin)
admin.site.register(order, oAdmin)
admin.site.register(customer, customerAdmin)
admin.site.register(address, addressAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
