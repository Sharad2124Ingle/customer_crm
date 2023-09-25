from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import RetailUser

class RetailUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone_no', 'shop_name', 'mall_name', 'is_staff')
    search_fields = ('username', 'email', 'phone_no', 'shop_name', 'mall_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'phone_no', 'shop_name', 'mall_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'phone_no', 'shop_name', 'mall_name'),
        }),
    )

admin.site.register(RetailUser, RetailUserAdmin)
