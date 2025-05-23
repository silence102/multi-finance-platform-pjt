<template>
    <div class="chat-window">
        <div class="chat-header">
            <span>AI 챗봇</span>
            <button class="close-btn" @click="$emit('close')">×</button>
        </div>

        <div class="chat-body">
            <div class="chat-bubble bot">
                안녕하세요! 무엇을 도와드릴까요?
            </div>

            <div class="chat-options">
                <div class="chat-bubble user-option" v-for="(option, index) in options" :key="index"
                    @click="selectOption(option)">
                    {{ option }}
                </div>
            </div>

            <div class="chat-bubble user" v-if="userMessage">
                {{ userMessage }}
            </div>
        </div>

        <!-- ✅ 입력창 영역 -->
        <div class="chat-input">
            <input type="text" v-model="input" placeholder="메시지를 입력하세요..." @keyup.enter="sendMessage" />
            <button @click="sendMessage">전송</button>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const options = [
    '투자를 시작하고 싶어',
    '핀트 투자가 궁금해',
    '수익률을 알고 싶어',
    '다른 투자자들이 궁금해',
    '다른 정보가 더 궁금해',
]

const input = ref('')
const userMessage = ref('')

const sendMessage = () => {
    if (input.value.trim()) {
        userMessage.value = input.value
        input.value = ''
    }
}

const selectOption = (text) => {
    userMessage.value = text
}
</script>

<style scoped>
.chat-window {
    position: fixed;
    bottom: 100px;
    right: 24px;
    width: 320px;
    background: #f2f2f2;
    border-radius: 20px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
    font-family: 'Pretendard', sans-serif;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    z-index: 999;
}

.chat-header {
    background: #0d6efd;
    color: white;
    padding: 12px 16px;
    font-weight: bold;
    display: flex;
    justify-content: space-between;
}

.close-btn {
    background: none;
    border: none;
    color: white;
    font-size: 18px;
    cursor: pointer;
}

.chat-body {
    padding: 16px;
    background: white;
    flex-grow: 1;
    overflow-y: auto;
}

.chat-bubble {
    display: inline-block;
    max-width: 80%;
    padding: 10px 14px;
    border-radius: 16px;
    font-size: 0.95rem;
    margin-bottom: 10px;
    line-height: 1.4;
}

.bot {
    background: #e6f0ff;
    color: #333;
}

.user {
    background: #d0ebff;
    color: #222;
    align-self: flex-end;
    margin-left: auto;
}

.user-option {
    background: #0d6efd;
    color: white;
    margin-left: auto;
    text-align: left;
    cursor: pointer;
    transition: background 0.3s;
}

.user-option:hover {
    background: #0b5ed7;
}

.chat-input {
    display: flex;
    padding: 12px;
    background: #f9f9f9;
    border-top: 1px solid #ccc;
}

.chat-input input {
    flex: 1;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 8px;
    margin-right: 8px;
    font-size: 0.95rem;
}

.chat-input button {
    background: #0d6efd;
    color: white;
    border: none;
    padding: 8px 12px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 0.95rem;
}
</style>
