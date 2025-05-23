<template>
  <div class="container mt-5" style="max-width: 400px">
    <h2 class="mb-4">로그인</h2>
    <form @submit.prevent="login">
      <div class="mb-3">
        <label for="username" class="form-label">아이디</label>
        <input type="text" class="form-control" id="username" v-model="username" />
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">비밀번호</label>
        <input type="password" class="form-control" id="password" v-model="password" />
      </div>
      <button type="submit" class="btn btn-success w-100">로그인</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const username = ref('')
const password = ref('')

const login = () => {
  console.log('로그인 요청', username.value, password.value)
}
</script>
