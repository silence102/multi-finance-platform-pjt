from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
  email = models.EmailField()
  age = models.PositiveIntegerField(null=True, blank=True)
  nickname = models.CharField(max_length=150, null=True, blank=True)
  salary = models.PositiveIntegerField(null=True, blank=True)
  assets = models.PositiveIntegerField(null=True, blank=True)
#   subscribed_products = models.TextField(blank=True, null=True, help_text="쉼표로 구분된 가입 상품 ID 목록")

  def save(self, *args, **kwargs):
    if not self.nickname:
        self.nickname = self.username
    super().save(*args, **kwargs)
        
#   def get_subscribed_products_list(self):
#     """
#     쉼표로 구분된 문자열을 리스트로 변환
#     """
#     if self.subscribed_products:
#         return self.subscribed_products.split(',')
#     return []

#   def add_product(self, product_id):
#     """
#     상품 ID를 가입 목록에 추가 (중복 방지)
#     """
#     current = set(self.get_subscribed_products_list())
#     current.add(str(product_id))
#     self.subscribed_products = ','.join(current)
#     self.save()
