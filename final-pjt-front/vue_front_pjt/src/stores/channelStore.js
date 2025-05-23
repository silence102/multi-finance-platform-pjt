// src/stores/channelStore.js
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useChannelStore = defineStore('channel', () => {
  const savedChannels = ref([])

  // 최초 로드 시 localStorage에서 데이터 불러오기
  const loadChannels = () => {
    const raw = localStorage.getItem('savedChannels')
    savedChannels.value = raw ? JSON.parse(raw) : []
  }

  const saveChannel = (channelName) => {
    if (!savedChannels.value.includes(channelName)) {
      savedChannels.value.push(channelName)
      localStorage.setItem('savedChannels', JSON.stringify(savedChannels.value))
    }
  }

  const removeChannel = (channelName) => {
    savedChannels.value = savedChannels.value.filter(c => c !== channelName)
    localStorage.setItem('savedChannels', JSON.stringify(savedChannels.value))
  }

  const isSaved = (channelName) => {
    return savedChannels.value.includes(channelName)
  }

  return {
    savedChannels,
    loadChannels,
    saveChannel,
    removeChannel,
    isSaved,
  }
})
