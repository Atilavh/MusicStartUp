from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', views.register_view, name='account-register'),
    path('verify/', views.verify_view, name='account-verify'),
    path('login/', views.login_view, name='account-login'),
    path('logout/', views.logout_view, name='account-logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]

