from django.urls import path, include
from .views import RegisterView, UserView
from rest_framework_simplejwt.views import TokenRefreshView, TokenRefreshSlidingView, TokenObtainPairView

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshSlidingView.as_view()),
    path('auth/me/', UserView.as_view()),
]

