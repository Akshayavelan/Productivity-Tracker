from django.urls import path
from .views import ProfileView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup', ProfileView.as_view(),name='signup'),
    path('login', CustomTokenObtainPairView.as_view(),name='login'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]