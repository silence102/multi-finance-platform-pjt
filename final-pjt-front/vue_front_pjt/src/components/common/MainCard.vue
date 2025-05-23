<!-- src/components/MainCard.vue -->
<template>
    <div class="card h-100 shadow-sm">
        <div class="card-body">
            <h5 class="card-title fw-bold mb-3">{{ title }}</h5>
            <slot />
        </div>
    </div>
</template>

<script setup>
defineProps({
    title: String,
})
</script>

<style scoped>
.card {
    border-radius: 16px;
    background-color: #f9f9f9;
}
</style>
