from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Deposit, Saving
from .serializers import DepositDetailSerializer, SavingDetailSerializer
from django.conf import settings
import requests


# 예금 상품 DB에 저장하기
class FetchDepositInstitutionsView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        api_key = settings.FSS_API_KEY
        url = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            base_list = data.get("result", {}).get("baseList", [])
            option_list = data.get("result", {}).get("optionList", [])

            # 먼저 상품 기본 정보 저장
            for item in base_list:
                Deposit.objects.update_or_create(
                    fin_prdt_cd=item["fin_prdt_cd"],
                    defaults={
                        "fin_prdt_cd": item.get("fin_prdt_cd", ""),
                        "dcls_month": item.get("dcls_month", ""),
                        "fin_co_no": item.get("fin_co_no", ""),
                        "kor_co_nm": item.get("kor_co_nm", ""),
                        "fin_prdt_nm": item.get("fin_prdt_nm", ""),
                        "join_deny": item.get("join_deny", ""),
                        "join_member": item.get("join_member", ""),
                        "mtrt_int": item.get("mtrt_int", ""),
                        "max_limit": item.get("max_limit", ""),
                        "join_way": item.get("join_way", ""),
                        "spcl_cnd": item.get("spcl_cnd", ""),
                    },
                )

            # 다음으로 금리 옵션 반영 (상품코드로 매칭)
            for option in option_list:
                prdt_cd = option.get("fin_prdt_cd")
                deposit = Deposit.objects.filter(fin_prdt_cd=prdt_cd).first()
                if deposit:
                    intr_rate_type = option.get("intr_rate_type_nm")
                    if intr_rate_type == "단리":  # 단리 상품만 처리
                        term = option.get("save_trm")  # 예: "6", "12"
                        rate = option.get("intr_rate")

                        if term == "6":
                            deposit.month_6 = rate
                        elif term == "12":
                            deposit.month_12 = rate
                        elif term == "24":
                            deposit.month_24 = rate
                        elif term == "36":
                            deposit.month_36 = rate

                        deposit.save()

            return Response(
                {"message": f"예금 상품 {len(base_list)}건 저장 완료"},
                status=status.HTTP_200_OK,
            )

        except requests.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# 적금 상품 DB에 저장
class FetchSavingInstitutionsView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        api_key = settings.FSS_API_KEY
        url = f"http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            base_list = data.get("result", {}).get("baseList", [])
            option_list = data.get("result", {}).get("optionList", [])

            # 1. 기본 상품 정보 저장
            for item in base_list:
                Saving.objects.update_or_create(
                    fin_prdt_cd=item["fin_prdt_cd"],
                    defaults={
                        "dcls_month": item.get("dcls_month", ""),
                        "fin_co_no": item.get("fin_co_no", ""),
                        "kor_co_nm": item.get("kor_co_nm", ""),
                        "fin_prdt_nm": item.get("fin_prdt_nm", ""),
                        "join_deny": item.get("join_deny", ""),
                        "join_member": item.get("join_member", ""),
                        "mtrt_int": item.get("mtrt_int", ""),
                        "max_limit": item.get("max_limit", ""),
                        "join_way": item.get("join_way", ""),
                        "spcl_cnd": item.get("spcl_cnd", ""),
                    },
                )

            # 2. 금리 옵션 정보 반영
            for option in option_list:
                prdt_cd = option.get("fin_prdt_cd")
                saving = Saving.objects.filter(fin_prdt_cd=prdt_cd).first()
                if saving:
                    intr_rate_type = option.get("intr_rate_type_nm")
                    if intr_rate_type == "단리":
                        term = option.get("save_trm")  # 예: "6", "12", "24", "36"
                        rate = option.get("intr_rate")

                        if term == "6":
                            saving.month_6 = rate
                        elif term == "12":
                            saving.month_12 = rate
                        elif term == "24":
                            saving.month_24 = rate
                        elif term == "36":
                            saving.month_36 = rate

                        saving.save()

            return Response(
                {"message": f"적금 상품 {len(base_list)}건 저장 완료"},
                status=status.HTTP_200_OK,
            )

        except requests.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# 1. 상품 상세 조회
class DepositDetailView(generics.RetrieveAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositDetailSerializer
    permission_classes = [permissions.AllowAny]


# 2. 상품 가입 / 가입취소
class DepositJoinToggleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        deposit = Deposit.objects.get(pk=pk)
        user = request.user
        deposit.deposit_joined_users.add(user)
        return Response({"message": "가입 완료"}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        deposit = Deposit.objects.get(pk=pk)
        user = request.user
        deposit.deposit_joined_users.remove(user)
        return Response({"message": "가입 취소"}, status=status.HTTP_200_OK)


# 3. 좋아요 / 좋아요 취소
class DepositLikeToggleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        deposit = Deposit.objects.get(pk=pk)
        user = request.user
        deposit.deposit_like_users.add(user)
        return Response({"message": "좋아요 추가"}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        deposit = Deposit.objects.get(pk=pk)
        user = request.user
        deposit.deposit_like_users.remove(user)
        return Response({"message": "좋아요 취소"}, status=status.HTTP_200_OK)


# 적금 상세 조회
class SavingDetailView(generics.RetrieveAPIView):
    queryset = Saving.objects.all()
    serializer_class = SavingDetailSerializer
    permission_classes = [permissions.AllowAny]


# 적금 가입 / 취소
class SavingJoinToggleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        saving = Saving.objects.get(pk=pk)
        saving.saving_joined_users.add(request.user)
        return Response({"message": "가입 완료"}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        saving = Saving.objects.get(pk=pk)
        saving.saving_joined_users.remove(request.user)
        return Response({"message": "가입 취소"}, status=status.HTTP_200_OK)


# 적금 좋아요 / 취소
class SavingLikeToggleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        saving = Saving.objects.get(pk=pk)
        saving.saving_like_users.add(request.user)
        return Response({"message": "좋아요 추가"}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        saving = Saving.objects.get(pk=pk)
        saving.saving_like_users.remove(request.user)
        return Response({"message": "좋아요 취소"}, status=status.HTTP_200_OK)
