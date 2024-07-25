from django.urls import path
from .views import dashboard, get_login_status, LoginStatusView

urlpatterns = [
    path('login-status/', get_login_status, name='login_status'),
    path('api/login-status/', LoginStatusView.as_view(), name='api_login_status'),
]
