from django.urls import path, include
from .views import CustomUserDetailView, CustomUserDeleteView
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path, include
from .views import CustomRegisterView

urlpatterns = [
  # 로그인, 로그아웃, 비밀번호 변경 등
  path('auth/', include('dj_rest_auth.urls')),

  # 회원가입 (Register)
  path('auth/registration/', CustomRegisterView.as_view(), name='custom_register'),

  path('profile/', CustomUserDetailView.as_view(), name='user-detail'),

  path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


  path('profile/delete/', CustomUserDeleteView.as_view(), name='user-delete'),

]
