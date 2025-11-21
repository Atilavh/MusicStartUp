from django.contrib import admin

from apps.account_app.models import User, OTP


# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "phone", "is_active", "is_staff", "is_superuser"]
    list_filter = ["is_active", "is_staff", "is_superuser"]
    search_fields = ["first_name", "last_name", "phone"]
    ordering = ["id"]

@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "code", "is_verified", "created_at"]
    list_filter = ["is_verified"]
    search_fields = ["user__phone"]
    ordering = ["-created_at"]