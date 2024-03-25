from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Unregister the CustomUser model if it's already registered
if admin.site.is_registered(CustomUser):
    admin.site.unregister(CustomUser)

# Register the CustomUser model with your CustomUserAdmin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    filter_horizontal = []
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    list_filter = ['is_staff', 'is_superuser']

admin.site.register(CustomUser, CustomUserAdmin)