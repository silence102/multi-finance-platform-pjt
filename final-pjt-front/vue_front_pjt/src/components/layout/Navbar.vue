<!-- src/components/layout/Navbar.vue -->
<template>
    <nav class="navbar navbar-expand-lg custom-navbar">
        <div class="container-fluid">
            <!-- 로고 -->
            <RouterLink class="navbar-brand text-orange fw-bold fs-4" :to="{ name: 'Home' }">FinView</RouterLink>

            <!-- 반응형 토글 -->
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>

            <!-- 메뉴 -->
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto gap-2">
                    <li v-for="(item, index) in navItems" :key="index" class="nav-item">
                        <RouterLink class="nav-link custom-link" :to="{ name: item.name }">
                            {{ item.label }}
                        </RouterLink>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script setup>
import { RouterLink } from 'vue-router'

const navItems = [
    { label: '예적금 비교', name: 'Products' },
    { label: '현물 시세', name: 'Asset' },
    { label: '관심 종목 검색', name: 'video' },
    { label: '은행 찾기', name: 'Bank' },
    { label: '커뮤니티', name: 'Community' },
    { label: '프로필 페이지', name: 'Profile' },
    { label: '회원가입', name: 'Signup' },
    { label: '로그인', name: 'Login' }
]
</script>

<style scoped>
.custom-navbar {
    background-color: #ffffff;
    border-bottom: 1px solid #eee;
}

.navbar-brand {
    color: #f26522 !important;
}

.custom-link {
    color: #333;
    font-weight: 500;
    transition: color 0.3s ease;
}

.custom-link:hover {
    color: #f26522;
    text-decoration: underline;
}
</style>
