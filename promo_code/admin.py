from django.contrib import admin
from promo_code.models import PromoCode, PromoCodeUser


@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ['time_mode', 'user_mode', 'promo_code', 'discount']
    readonly_fields = ['created_at']

    # def is_used(self, obj):
    #     pass
    # is_used.short_description = 'Был ли использован'
    #
    # def is_active(self, obj):
    #     pass
    # is_active.short_description = 'Активен ли'


@admin.register(PromoCodeUser)
class PromoCodeUserAdmin(admin.ModelAdmin):
    list_display = ['promo_code', 'user', 'active']
    readonly_fields = ['promo_code', 'user', 'active']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
