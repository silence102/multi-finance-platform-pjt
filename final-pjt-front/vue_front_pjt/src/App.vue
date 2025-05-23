<template>
  <div>
    <Navbar />
    <RouterView />
    <FooterBar />
  </div>
</template>

<script setup>
import Navbar from '@/components/layout/Navbar.vue'
import HomeView from '@/views/HomeView.vue'
import FooterBar from '@/components/layout/FooterBar.vue'
import { RouterLink, RouterView } from 'vue-router'

</script>

<style scoped>
body {
  margin: 0;
  padding: 0;
  font-family: 'Pretendard', sans-serif;
}
</style>