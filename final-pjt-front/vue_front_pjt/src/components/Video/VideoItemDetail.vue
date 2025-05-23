<template>
    <div class="detail-container">
        <router-link to="/search" class="back-link">← 뒤로가기</router-link>

        <h1 class="video-title">{{ video?.title || '영상 제목 없음' }}</h1>
        <p class="upload-date">업로드 날짜: {{ uploadDate }}</p>

        <div class="video-wrapper">
            <iframe :src="youtubeEmbedUrl" frameborder="0" allowfullscreen></iframe>
        </div>

        <p class="description">
            {{ video?.description || '설명 정보가 없습니다.' }}
        </p>

        <div class="action-buttons">
            <button @click="isSaved ? removeVideo() : saveVideo()" :class="isSaved ? 'remove-btn' : 'save-btn'">
                {{ isSaved ? '영상 저장 취소' : '동영상 저장' }}
            </button>

            <button @click="isChannelSaved ? removeChannel() : saveChannel()"
                :class="isChannelSaved ? 'remove-btn' : 'channel-btn'">
                {{ isChannelSaved ? '채널 저장 취소' : '채널 저장' }}
            </button>
        </div>
    </div>
    <br>
    <hr>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { useVideoStore } from '@/stores/videoStore'
import { ref, computed, onMounted } from 'vue'

const store = useVideoStore()
const route = useRoute()
const isSaved = ref(false)
const video = store.selectedVideo

// iframe용 embed URL 구성
const youtubeEmbedUrl = computed(() =>
    video ? `https://www.youtube.com/embed/${video.id}` : ''
)

// 예시: video.snippet.publishedAt 이 있다면 활용 가능
// 현재는 임시 날짜로 설정 (실제 데이터에 따라 수정)
const uploadDate = computed(() =>
    video?.uploadDate || '2025-03-24' // 실제 API에는 publishedAt 존재
)

function saveVideo() {
    const saved = JSON.parse(localStorage.getItem('savedVideos') || '[]')
    if (saved.some(v => v.id === video.id)) {
        alert('이미 저장된 영상입니다.')
        return
    }
    saved.push(video)
    localStorage.setItem('savedVideos', JSON.stringify(saved))
    isSaved.value = true // ✅ 상태 토글
    alert('✅ 저장되었습니다!')
}

function removeVideo() {
    const saved = JSON.parse(localStorage.getItem('savedVideos') || '[]')
    const updated = saved.filter(v => v.id !== video.id)
    localStorage.setItem('savedVideos', JSON.stringify(updated))
    isSaved.value = false // ✅ 상태 토글
    alert('❌ 저장 취소되었습니다.')
}


const isChannelSaved = ref(false)

onMounted(() => {
    const savedVideos = JSON.parse(localStorage.getItem('savedVideos') || '[]')
    isSaved.value = savedVideos.some(v => v.id === video.id)

    const savedChannels = JSON.parse(localStorage.getItem('savedChannels') || '[]')
    isChannelSaved.value = savedChannels.includes(video.channelTitle)
})

function saveChannel() {
    const saved = JSON.parse(localStorage.getItem('savedChannels') || '[]')
    if (!saved.includes(video.channelTitle)) {
        saved.push(video.channelTitle)
        localStorage.setItem('savedChannels', JSON.stringify(saved))
        isChannelSaved.value = true
        alert('채널 저장 완료')
    }
}

function removeChannel() {
    const saved = JSON.parse(localStorage.getItem('savedChannels') || '[]')
    const updated = saved.filter(c => c !== video.channelTitle)
    localStorage.setItem('savedChannels', JSON.stringify(updated))
    isChannelSaved.value = false
    alert('채널 저장 취소됨')
}

</script>

<style scoped>
.detail-container {
    max-width: 800px;
    margin: 40px auto;
    padding: 0 20px;
    font-family: 'Arial', sans-serif;
}

.back-link {
    display: inline-block;
    margin-bottom: 20px;
    color: #555;
    text-decoration: none;
    font-size: 14px;
}

.video-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
}

.upload-date {
    color: #888;
    margin-bottom: 20px;
}

.video-wrapper iframe {
    width: 100%;
    height: 400px;
    margin-bottom: 20px;
}

.description {
    font-size: 16px;
    line-height: 1.6;
    margin-bottom: 30px;
}

.save-btn {
    background-color: #ff2e63;
    color: white;
    border: none;
    padding: 12px 20px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 14px;
}

.save-btn:hover {
    background-color: #ff2e63;
}

/* 버튼 묶음 정렬 */
.action-buttons {
    display: flex;
    gap: 10px;
    margin-top: 20px;
    flex-wrap: wrap;
}

/* 중복된 .description 제거 → 하나로 */
.description {
    font-size: 16px;
    line-height: 1.6;
    margin-bottom: 30px;
    white-space: pre-line;
}


.channel-btn,
.remove-btn {
    padding: 10px 18px;
    font-size: 14px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    transition: background-color 0.2s ease;
    color: white;
}

.channel-btn {
    background-color: #f0ad4e;
    /* 주황 계열 */
}

.channel-btn:hover {
    background-color: #ec971f;
}

.remove-btn {
    background-color: #6c757d;
    /* 회색 계열 */
}

.remove-btn:hover {
    background-color: #5a6268;
}
</style>
