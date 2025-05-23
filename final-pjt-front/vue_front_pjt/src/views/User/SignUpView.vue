<template>
  <div class="container mt-5" style="max-width: 500px">
    <h2 class="mb-4">회원가입</h2>
    <form @submit.prevent="signUp">
      <div v-for="(field, key) in form" :key="key" class="mb-3">
        <label :for="key" class="form-label">{{ field.label }}</label>
        <input :type="field.type" class="form-control" :id="key" v-model="field.value" />
      </div>
      <button type="submit" class="btn btn-primary w-100">가입하기</button>
    </form>
  </div>
</template>

<script setup>
import { reactive } from 'vue'

const form = reactive({
  username: { label: '아이디', type: 'text', value: '' },
  password1: { label: '비밀번호', type: 'password', value: '' },
  password2: { label: '비밀번호 확인', type: 'password', value: '' },
  email: { label: '이메일', type: 'email', value: '' },
  age: { label: '나이', type: 'number', value: '' },
  nickname: { label: '닉네임', type: 'text', value: '' },
})

const signUp = () => {
  console.log('회원가입 요청', form)
}
</script>
