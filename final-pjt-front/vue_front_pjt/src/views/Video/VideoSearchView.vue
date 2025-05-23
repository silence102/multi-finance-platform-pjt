<template>
    <header>
        <nav class="navbar">
            <RouterLink :to="{ name: 'main' }" class="nav-link">MyTube</RouterLink>
            <RouterLink :to="{ name: 'home' }" class="nav-link">Home</RouterLink>
            <RouterLink :to="{ name: 'search' }" class="nav-link">Search</RouterLink>
            <RouterLink :to="{ name: 'later' }" class="nav-link">Later</RouterLink>
            <RouterLink :to="{ name: 'channel' }" class="nav-link">Channel</RouterLink>
        </nav>
        <RouterView />
    </header>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Home from '@/components/Home.vue'
</script>

<style>
html,
body {
    height: 100%;
    margin: 0;
    padding: 0;
    overflow-y: auto;
    /* ✅ 세로 스크롤 허용 */
}
</style>

<style scoped>
.navbar {
    background-color: #000;
    /* 검은 배경 */
    padding: 15px 20px;
    /* 위아래, 좌우 여백 */
    display: flex;
    gap: 15px;
    /* 메뉴 간 간격 */
    align-items: center;
}

.nav-link {
    font-size: 24px;
    font-weight: bold;
    color: #ff2e63;
    text-decoration: none;
    padding: 4px 12px;
    border-radius: 6px;
    transition: background-color 0.2s ease, color 0.2s ease;
}

.nav-link:hover {
    background-color: #ff2e63;
    color: white;
}
</style>
