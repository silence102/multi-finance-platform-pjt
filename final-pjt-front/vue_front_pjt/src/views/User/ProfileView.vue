<template>
    <div class="container mt-5" style="max-width: 600px">
        <h2 class="mb-4">프로필 페이지</h2>

        <div class="profile-box mb-4">
            <h5 class="fw-bold">기본 정보</h5>
            <ul class="list-group mt-2">
                <li class="list-group-item"><strong>아이디:</strong> user123</li>
                <li class="list-group-item"><strong>이메일:</strong> user@example.com</li>
                <li class="list-group-item"><strong>나이:</strong> 26</li>
                <li class="list-group-item"><strong>닉네임:</strong> 민석이</li>
            </ul>
            <button class="btn btn-outline-primary mt-3">정보 수정</button>
        </div>

        <div class="profile-box">
            <h5 class="fw-bold">가입한 금융 상품</h5>
            <p class="text-muted mt-2">가입한 상품이 없습니다.</p>
            <!-- 추후 가입 상품 리스트 출력 예정 -->
        </div>
        <RouterLink :to="{ name: 'later' }">Later</RouterLink> |
        <RouterLink :to="{ name: 'channel' }">Channel</RouterLink>
        <RouterView />
    </div>
</template>

<script setup>
// 추후 사용자 데이터를 props 또는 pinia 등에서 가져와 동적으로 바인딩할 수 있습니다.
import { RouterLink, RouterView } from 'vue-router'

</script>

<style scoped>
.profile-box {
    background-color: #f8f9fa;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}
</style>
