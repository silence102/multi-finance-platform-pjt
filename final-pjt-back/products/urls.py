from django.urls import path
from . import views
from .views import FetchDepositInstitutionsView, FetchSavingInstitutionsView

urlpatterns = [
    path(
        "savings/fetch-institutions/",
        FetchSavingInstitutionsView.as_view(),
        name="fetch-saving-institutions",
    ),
    path(
        "deposits/fetch-institutions/",
        FetchDepositInstitutionsView.as_view(),
        name="fetch-deposit-institutions",
    ),
    # 상세 조회
    path(
        "deposits/<int:pk>/", views.DepositDetailView.as_view(), name="deposit-detail"
    ),
    # 가입 & 가입취소
    path(
        "deposits/<int:pk>/join/",
        views.DepositJoinToggleView.as_view(),
        name="deposit-join",
    ),
    # 좋아요 & 좋아요취소
    path(
        "deposits/<int:pk>/like/",
        views.DepositLikeToggleView.as_view(),
        name="deposit-like",
    ),
    path("savings/<int:pk>/", views.SavingDetailView.as_view(), name="saving-detail"),
    path(
        "savings/<int:pk>/join/",
        views.SavingJoinToggleView.as_view(),
        name="saving-join",
    ),
    path(
        "savings/<int:pk>/like/",
        views.SavingLikeToggleView.as_view(),
        name="saving-like",
    ),
]
