from django.contrib import admin
from subscribe.models import SubPrice, Subscribe


@admin.register(SubPrice)
class SubPriceAdmin(admin.ModelAdmin):
    list_display = ['name', 'value', 'duration']


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['user', 'start_date', 'end_date', 'is_active']
    readonly_fields = ['user', 'sub_price']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
