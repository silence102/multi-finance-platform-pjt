from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import CustomUser
from products.models import Deposit, Saving

class CustomUserSerializer(serializers.ModelSerializer):
    deposit_join_products = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True
    )
    saving_join_products = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True
    )
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'age', 'salary', 'assets', 'deposit_join_products', 'saving_join_products','nickname')

class CustomRegisterSerializer(RegisterSerializer):
  username = serializers.CharField(required=True)
  email = serializers.EmailField(required=True)
  age = serializers.IntegerField(required=True)
  salary = serializers.IntegerField(required=False)
  assets = serializers.IntegerField(required=False)
  nickname = serializers.CharField(required=False, allow_blank=True)

  def validate(self, data):
    data = super().validate(data)
    data['age'] = self.initial_data.get('age')
    data['salary'] = self.initial_data.get('salary')
    data['assets'] = self.initial_data.get('assets')
    data['nickname'] = self.initial_data.get('nickname') or self.initial_data.get('username')
    print("✅ initial_data:", self.initial_data)
    return data
  
  def get_cleaned_data(self):
    data = super().get_cleaned_data()
    data['username'] = self.validated_data.get('username', '')
    data['email'] = self.validated_data.get('email', '')
    data['age'] = self.validated_data.get('age', None)
    data['salary'] = self.validated_data.get('salary', None)
    data['assets'] = self.validated_data.get('assets', None)
    data['nickname'] = self.validated_data.get('nickname', self.validated_data.get('username', ''))
    print(data)
    return data

  def save(self, request):
    cleaned_data = self.get_cleaned_data()  # ✅ 여기서 값을 추출

    print("✅ save called with cleaned_data:", cleaned_data)

    user = super().save(request)
    user.age = int(cleaned_data.get('age') or 0)
    user.salary = int(cleaned_data.get('salary') or 0)
    user.assets = int(cleaned_data.get('assets') or 0)
    user.nickname = cleaned_data.get('nickname') or user.username
    user.save()
    return user


