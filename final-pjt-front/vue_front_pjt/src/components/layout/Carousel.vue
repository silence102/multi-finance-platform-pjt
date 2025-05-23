<template>
    <div id="Carousel" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
            <div :class="['carousel-item', item.className, { active: index === 0 }]" v-for="(item, index) in items"
                :key="index">
                <!-- ✅ 카드 스타일을 입힌 내부 콘텐츠 -->
                <div class="carousel-box">
                    <div class="text-center">
                        <h4 class="fw-bold text-dark">{{ item.title }}</h4>
                        <p class="fs-5">{{ item.description }}</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- 좌우 이동 버튼 -->
        <button class="carousel-control-prev" type="button" data-bs-target="#Carousel" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#Carousel" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
    </div>
</template>

<script setup>
const items = [
    { title: '카카오', description: '카카오 관련 최신 정보 요약', className: 'bg-kakao' },
    { title: '삼성전자', description: '삼성전자 최근 뉴스 & 유튜브', className: 'bg-samsung' },
    { title: '네이버', description: '네이버 관련 영상과 종목 분석', className: 'bg-naver' },
]
</script>

<style scoped>
.carousel-item {
    transition: transform 0.5s ease;
}

.carousel-box {
    height: 300px;
    border-radius: 16px;
    border: 3px solid #555;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
    transition: all 0.5s ease;
    display: flex;
    justify-content: center;
    align-items: center;
}

/* 배경색 강조 */
.bg-kakao {
    background-color: #fff3cd;
}

.bg-samsung {
    background-color: #cce5ff;
}

.bg-naver {
    background-color: #d4edda;
}
</style>
