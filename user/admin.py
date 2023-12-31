from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import User, OTPRequest

# Register your models here.

admin.site.register(OTPRequest)


@admin.register(User)
class DjshopUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
