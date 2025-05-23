<template>
    <div class="container">
        <h1>✨ 내가 좋아하는 채널</h1>

        <div v-if="channels.length === 0" class="empty-message">
            😢 저장된 채널이 아직 없습니다.
        </div>

        <ul v-else class="channel-list">
            <li v-for="channel in channels" :key="channel" class="channel-card">
                <div class="channel-info">
                    <span class="emoji">📺</span>
                    <span class="channel-name">{{ channel }}</span>
                </div>
                <button class="delete-btn" @click="remove(channel)">
                    💣 폭파
                </button>
            </li>
        </ul>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const channels = ref([])

onMounted(() => {
    const raw = localStorage.getItem('savedChannels')
    const parsed = raw ? JSON.parse(raw) : []
    channels.value = parsed.filter(c => c && c.trim() !== '')
})

function remove(channel) {
    const updated = channels.value.filter(c => c !== channel)
    channels.value = updated
    localStorage.setItem('savedChannels', JSON.stringify(updated))
}
</script>

<style scoped>
.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 60px 20px;
    font-family: 'Segoe UI', Tahoma, sans-serif;
    text-align: center;
}

h1 {
    font-size: 26px;
    margin-bottom: 32px;
    color: #222;
}

.empty-message {
    font-size: 18px;
    color: #888;
}

.channel-list {
    list-style: none;
    padding: 0;
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.channel-card {
    background-color: #fafafa;
    border: 1px solid #eee;
    border-radius: 10px;
    padding: 16px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
    transition: transform 0.2s ease;
}

.channel-card:hover {
    transform: translateY(-4px);
    background-color: #fffefc;
}

.channel-info {
    display: flex;
    align-items: center;
    gap: 10px;
}

.emoji {
    font-size: 22px;
}

.channel-name {
    font-size: 16px;
    font-weight: 500;
    color: #333;
}

.delete-btn {
    background-color: #f14668;
    border: none;
    border-radius: 6px;
    padding: 6px 10px;
    color: white;
    font-size: 14px;
    cursor: pointer;
    transition: background-color 0.2s ease;
}

.delete-btn:hover {
    background-color: #d42f51;
}
</style>