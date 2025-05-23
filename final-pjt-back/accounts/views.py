from django.shortcuts import render
# Create your views here.
from rest_framework import generics, permissions, status
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer

class CustomUserDetailView(generics.RetrieveUpdateAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = CustomUserSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_object(self):
      # 현재 로그인한 사용자 객체 반환
      return self.request.user
    
class CustomUserDeleteView(APIView):
  permission_classes = [IsAuthenticated]
        
  def delete(self, request):
        user = request.user
        user.delete()
        return Response({"message": "회원 탈퇴 완료"}, status=status.HTTP_204_NO_CONTENT)
      


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
