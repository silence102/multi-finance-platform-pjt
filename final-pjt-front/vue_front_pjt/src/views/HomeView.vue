<!-- MainLayout.vue (전체 메인 페이지 구조 구성) -->
<template>
    <div>
        <!-- ✅ 메인 카드 영역 -->
        <div class="home-container">
            <h2 class="title">홈 페이지입니다.</h2>

            <div class="card-grid">
                <RouterLink to="/products" class="card-link">
                    <div class="card-box bg-highlight">
                        <h5>주요 상품 정보</h5>
                        <p>인기 금융 상품 또는 추천 상품을 보여줍니다.</p>
                    </div>
                </RouterLink>

                <RouterLink to="/asset" class="card-link">
                    <div class="card-box bg-lightblue">
                        <h5>현물 시세 차트</h5>
                        <p>금/은 가격 차트를 시각적으로 보여줍니다.</p>
                    </div>
                </RouterLink>

                <RouterLink to="/bank" class="card-link">
                    <div class="card-box bg-gray">
                        <h5>근처 은행 찾기</h5>
                        <p>지도 기반으로 근처 은행을 검색합니다.</p>
                    </div>
                </RouterLink>

                <RouterLink to="/stock" class="card-link">
                    <div class="card-box bg-mint">
                        <h5>관심 종목 정보</h5>
                        <p>유튜브 영상, 종목 뉴스, 관련 데이터를 제공합니다.</p>
                    </div>
                </RouterLink>
            </div>
        </div>

        <!-- ✅ 캐러셀 (관심 종목 기반 정보 추천) -->
        <div class="container mt-5">
            <Carousel />
        </div>

        <ChatbotButton @toggle="toggleChat" />
        <ChatbotWindow v-if="isChatOpen" @close="toggleChat" />

        <!-- ✅ 푸터 -->
        <FooterBar />
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'

import ChatbotButton from '@/components/chatbot/ChatbotButton.vue'
import ChatbotWindow from '@/components/chatbot/ChatbotWindow.vue'
import Navbar from '@/components/layout/Navbar.vue'
import MainCard from '@/components/common/MainCard.vue'
import Carousel from '@/components/layout/Carousel.vue'
// import FooterBar from '@/components/layout/FooterBar.vue'

const isChatOpen = ref(false)
function toggleChat() {
    isChatOpen.value = !isChatOpen.value
}
</script>

<style scoped>
.home-container {
    padding: 32px 16px;
    max-width: 960px;
    margin: 0 auto;
}

.title {
    text-align: center;
    font-weight: bold;
    margin-bottom: 32px;
}

.card-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    /* ✅ 항상 2개씩 */
    gap: 20px;
}

@media (max-width: 640px) {
    .card-grid {
        grid-template-columns: 1fr;
        /* ✅ 모바일에서 1개씩 */
    }
}

.card-link {
    text-decoration: none;
    color: inherit;
}

.card-box {
    border-radius: 16px;
    padding: 24px;
    height: 180px;
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.1);
    background-color: #f9f9f9;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card-box:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
}

/* 배경 강조 */
.bg-highlight {
    background-color: #fff3cd;
}

.bg-lightblue {
    background-color: #cce5ff;
}

.bg-gray {
    background-color: #e2e3e5;
}

.bg-mint {
    background-color: #d4edda;
}
</style>
