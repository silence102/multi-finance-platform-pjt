<template>
    <div class="container">
        <!-- <router-link to="/" class="back-link">← 뒤로가기</router-link> -->
        <h1>나중에 볼 동영상</h1>

        <div v-if="savedVideos.length === 0">
            등록된 비디오 없음
        </div>

        <div v-else class="video-list">
            <div class="video-item-wrapper" v-for="video in savedVideos" :key="video.id">
                <VideoItem :video="video" />
                <button class="delete-btn" @click="removeVideo(video.id)">🧹 제거</button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import VideoItem from '@/components/Video/VideoItem.vue'

const savedVideos = ref([])

onMounted(() => {
    const raw = localStorage.getItem('savedVideos')
    savedVideos.value = raw ? JSON.parse(raw) : []
})

function removeVideo(id) {
    const updated = savedVideos.value.filter(v => v.id !== id)
    savedVideos.value = updated
    localStorage.setItem('savedVideos', JSON.stringify(updated))
}
</script>

<style scoped>
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 24px;
    /* ← 좌우 여백 */
}

.video-list {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    margin-top: 20px;
    justify-content: center;
    /* ← 옵션: 카드들을 가운데로 모으기 */
}

/* 카드 전체 */
.video-item-wrapper {
    width: 300px;
    border-radius: 8px;
    overflow: hidden;
    /* ✅ 버튼이 자연스럽게 안에 붙어 보이도록 */
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    background-color: #fff;
    display: flex;
    flex-direction: column;
}


.video-card {
    display: flex;
    flex-direction: column;
    justify-content: space-between;

    height: 100%;
    background-color: #fff;
    padding: 12px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.video-card img {
    width: 100%;
    border-radius: 6px;
}

/* 제목 텍스트 높이 고정 */
.video-title {
    font-size: 15px;
    font-weight: 500;
    margin: 10px 0;
    min-height: 3.6em;
    /* ✅ 약 3줄 정도 공간 확보 */
    line-height: 1.2em;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* 삭제 버튼 */
.delete-btn {
    width: 100%;
    /* ✅ 카드 아래 가로 전체 */
    padding: 10px;
    font-size: 14px;
    color: white;
    background-color: #dc3545;
    border: none;
    border-top: 1px solid #eee;
    /* ✅ 위와 구분 */
    cursor: pointer;
    border-radius: 0;
    /* ✅ 카드 경계와 맞춤 */
}

.delete-btn:hover {
    background-color: #b02a37;
}
</style>