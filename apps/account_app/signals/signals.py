from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.account_app.models import User
from apps.user_app.models import UserPermission


@receiver(post_save, sender=User)
def create_user_permission(sender, instance, created, **kwargs):
    if created:
        UserPermission.objects.create(user=instance)
