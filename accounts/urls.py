from django.urls import path
from .views import RegisterView, CustomTokenView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', CustomTokenView.as_view()),   # 🔥 IMPORTANT
    path('token/refresh/', TokenRefreshView.as_view()),
]