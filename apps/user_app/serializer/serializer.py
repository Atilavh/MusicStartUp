from rest_framework import serializers
from apps.account_app.models import User
from apps.user_app.models import UserPermission



# region UserListSerializer
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone',
            'is_staff',
            'is_superuser',
            'is_active'
        ]
# endregion


# region UserPermissionSerializer
class UserPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPermission
        fields = [
            'can_play_song',
            'can_create_playlist',
            'can_play_playlist',
            'can_download',
            'can_login'
        ]
        extra_kwargs = {
            field: {"required": False}
            for field in fields
        }
# endregion