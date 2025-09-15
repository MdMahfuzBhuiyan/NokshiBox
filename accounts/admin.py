from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import path
from django.http import HttpResponseForbidden
from .models import User
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'full_name', 'mobile', 'role', 'is_active']
    ordering = ['-date_joined']
    readonly_fields = ['date_joined', 'last_login']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
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

    
    def change_view(self, request, object_id, form_url='', extra_context=None):
        if extra_context is None:
            extra_context = {}
        extra_context['show_change_password'] = False  # hides the link in UI
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

   
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<id>/password/', self.block_password_change)
        ]
        return custom_urls + urls

    def block_password_change(self, request, id):
        return HttpResponseForbidden("Password reset via admin is disabled.")

# Register your custom UserAdmin
admin.site.register(User, CustomUserAdmin)
