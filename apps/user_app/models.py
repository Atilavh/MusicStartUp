from django.db import models
from apps.account_app.models import User
from django_jalali.db import models as jmodels

# region UserPermissionModel
class UserPermission(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_permission')
    # TODO: USER_PERMISSIONS--------------------
    can_play_song = models.BooleanField(default=True, verbose_name='Can play song')
    can_create_playlist = models.BooleanField(default=True, verbose_name='Can create playlist')
    can_play_playlist = models.BooleanField(default=True, verbose_name='Can play playlist')
    can_download = models.BooleanField(default=True, verbose_name='Can download')
    can_login = models.BooleanField(default=True, verbose_name='Can login')
    # TODO: USER_PERMISSIONS--------------------
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='Created at')

    class Meta:
        verbose_name = 'User Permission'
        verbose_name_plural = 'User Permissions'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"Permissions for {self.user.phone}"
# endregion