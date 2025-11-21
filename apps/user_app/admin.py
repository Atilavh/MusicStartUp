from django.contrib import admin
from apps.user_app.models import UserPermission


@admin.register(UserPermission)
class UserPermissionAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "can_play_song",
        "can_create_playlist",
        "can_play_playlist",
        "can_download",
        "can_login"
    ]
    list_filter = [
        "can_play_song",
        "can_create_playlist",
        "can_play_playlist",
        "can_download",
        "can_login"
    ]
    search_fields = ["user__phone"]
