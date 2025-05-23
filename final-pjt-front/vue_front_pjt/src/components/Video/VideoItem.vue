<template>
    <div class="video-card" @click="goToDetail(video)">
        <img :src="video.thumbnail" alt="썸네일" />
        <p class="video-title">{{ decodedTitle }}</p>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useVideoStore } from '@/stores/videoStore'
import { computed } from 'vue'

const props = defineProps({
    video: Object
})

const router = useRouter()
const videoStore = useVideoStore()

function goToDetail(video) {
    videoStore.selectedVideo = video
    router.push({ name: 'videoDetail', params: { id: video.id } })
}

function decodeHtml(html) {
    const txt = document.createElement('textarea')
    txt.innerHTML = html
    return txt.value
}

const decodedTitle = computed(() => decodeHtml(props.video.title))
</script>

<style scoped>
.video-card {
    width: 300px;
    background-color: #fff;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
    overflow: hidden;
    transition: transform 0.2s ease;
    cursor: pointer;
}

.video-card:hover {
    transform: translateY(-4px);
}

.video-card img {
    width: 100%;
    height: auto;
}

.video-title {
    padding: 12px 16px;
    /* ✅ 썸네일과 텍스트 사이 여백 */
    font-size: 15px;
    font-weight: 500;
}
</style>
