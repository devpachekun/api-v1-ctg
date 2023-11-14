from django.urls import path
from rest_framework_simplejwt.views import (TokenRefreshView)
from . import views

# Custom Access Token
from .views import MyTokenObtainPairView

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='api-token-auth'),
    path('login/user/refresh-token/', TokenRefreshView.as_view(), name='api-token-refresh'),
]
