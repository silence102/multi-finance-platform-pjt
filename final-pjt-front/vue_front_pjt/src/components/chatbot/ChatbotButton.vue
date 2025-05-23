<template>
    <button class="chatbot-btn" @click="$emit('toggle')">🤖</button>
</template>

<style scoped>
.chatbot-btn {
    position: fixed;
    bottom: 24px;
    right: 24px;
    background-color: #0d6efd;
    color: white;
    border: none;
    border-radius: 50%;
    width: 56px;
    height: 56px;
    font-size: 24px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    cursor: pointer;
    z-index: 1000;
}
</style>
