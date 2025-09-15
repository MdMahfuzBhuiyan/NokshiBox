from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'full_name', 'mobile','role','is_active']
    ordering = ['-date_joined']
admin.site.register(User,CustomUserAdmin)
