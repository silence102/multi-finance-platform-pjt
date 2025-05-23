// stores/videoStore.js
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useVideoStore = defineStore('video', () => {
  const selectedVideo = ref(null)
  return { selectedVideo }
})
