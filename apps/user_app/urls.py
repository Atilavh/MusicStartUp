from django.urls import path
from . import views

urlpatterns = [
        path('users/', views.user_list_view, name='user-list'),
        path('users/<int:user_id>/permissions/', views.user_permission_view, name='user-permissions'),
]