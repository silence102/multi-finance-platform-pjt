from rest_framework import serializers

from .models import Deposit, Saving


#  목록 조회
class DepositListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = [
            "dcls_month",
            "fin_prdt_cd",
            "kor_co_nm",
            "fin_prdt_nm",
            "month_6",
            "month_12",
            "month_24",
            "month_36",
            "deposit_like_users",
        ]


# 적금
class SavingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = [
            "dcls_month",
            "fin_prdt_cd",
            "kor_co_nm",
            "fin_prdt_nm",
            "month_6",
            "month_12",
            "month_24",
            "month_36",
            "saving_like_users",
        ]


# 상세 조회
class DepositDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = "__all__"

    def get_like_count(self, obj):
        return obj.deposit_like_users.count()


class SavingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = "__all__"

    def get_like_count(self, obj):
        return obj.saving_like_users.count()
