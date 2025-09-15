from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'full_name', 'mobile', 'role', 'is_active']
    ordering = ['-date_joined']
    readonly_fields = ['date_joined', 'last_login']

    fieldsets = (
        (None, {'fields': ('email',)}),  
        (_('Personal info'), {'fields': ('full_name', 'mobile', 'role')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'mobile', 'role', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )

    search_fields = ('email', 'full_name', 'mobile')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if 'password' in form.base_fields:
            del form.base_fields['password']  
        return form

admin.site.register(User, CustomUserAdmin)
