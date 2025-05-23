<template>
    <div class="container">
        <router-link to="/" class="back-link">뒤로가기</router-link>
        <h1>비디오 검색</h1>
        <form @submit.prevent="searchVideos">
            <input type="text" v-model="query" placeholder="검색어 입력" />
            <button>찾기</button>
        </form>

        <div class="page-container">
            <div class="video-section">
                <template v-if="videos.length > 0">
                    <VideoItem v-for="video in videos" :key="video.id" :video="video" class="video-card" />
                </template>
                <template v-else>
                    <div class="empty-state">
                        <p>🔍 검색 결과가 없습니다.</p>
                    </div>
                </template>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import VideoItem from '@/components/Video/VideoItem.vue'

const query = ref('')
const videos = ref([])

onMounted(() => {
    // 🔁 저장된 검색어와 결과 복원
    const prevQuery = localStorage.getItem('searchQuery')
    const prevVideos = localStorage.getItem('searchResults')

    if (prevQuery) query.value = prevQuery
    if (prevVideos) videos.value = JSON.parse(prevVideos)

    setTimeout(() => {
        document.querySelector('input[type="text"]')?.focus()
    }, 300)

})

// REST API 호출
async function searchVideos() {
    const apiKey = "AIzaSyBVDfxA1MPiVGORJ4vaVwWne8yP9Vb8wLg"
    const maxResults = 12
    const searchQuery = query.value

    const response = await fetch(
        `https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&maxResults=${maxResults}&q=${encodeURIComponent(searchQuery)}&key=${apiKey}`
    )
    const data = await response.json()
    console.log("API 응답 데이터:", data)

    const videoIds = data.items
        .filter(item => item.id.kind === 'youtube#video')
        .map(item => item.id.videoId)
        .join(',')

    const detailsRes = await fetch(
        `https://www.googleapis.com/youtube/v3/videos?part=snippet&id=${videoIds}&key=${apiKey}`
    )
    const detailsData = await detailsRes.json()

    videos.value = detailsData.items.map(item => ({
        id: item.id,
        title: item.snippet.title,
        thumbnail: item.snippet.thumbnails.medium.url,
        description: item.snippet.description, // ← 이제 전체 설명이 들어옴
        channelTitle: item.snippet.channelTitle
    }))
    // ✅ 검색어와 결과 저장
    localStorage.setItem('searchQuery', query.value)
    localStorage.setItem('searchResults', JSON.stringify(videos.value))
}
</script>

<style scoped>
/* 전체 폰트 스타일 */
* {
    box-sizing: border-box;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

body {
    background-color: #f9f9f9;
    line-height: 1.5;
}

.video-list {
    display: flex;
    flex-wrap: wrap;
    gap: 24px;
    margin-top: 30px;
}

.video-card {
    width: 300px;
    background-color: #fff;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    transition: transform 0.2s ease;
}

.video-card:hover {
    transform: translateY(-6px);
}

.video-card img {
    width: 100%;
    height: auto;
}

.video-card p {
    padding: 10px 16px;
    font-weight: 500;
    font-size: 15px;
}

form {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-top: 20px;
}

input[type="text"] {
    padding: 10px 14px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 6px;
    width: 500px;
}

button {
    padding: 10px 18px;
    font-size: 16px;
    background-color: #ff2e63;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    transition: background-color 0.2s ease;
}

button:hover {
    background-color: #ff2e63;
}

h1 {
    font-size: 28px;
    margin-top: 20px;
}

.back-link {
    display: inline-block;
    margin-top: 10px;
    font-size: 14px;
    color: #555;
    text-decoration: none;
}

.back-link:hover {
    text-decoration: underline;
}

.container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 40px 20px;
}

.page-container {
    display: flex;
    justify-content: center;
    padding: 40px 0;
    background-color: #f9f9f9;
}

.video-section {
    max-width: 2000px;
    width: 100%;
    padding: 0 40px;
    display: flex;
    flex-wrap: wrap;
    gap: 24px;

    border-left: 1px solid #ddd;
    /* ✅ 좌측 선 */
    border-right: 1px solid #ddd;
    /* ✅ 우측 선 */
    background-color: #fff;
}

.empty-state {
    width: 100%;
    padding: 100px 0;
    text-align: center;
    color: #777;
    font-size: 18px;
}
</style>