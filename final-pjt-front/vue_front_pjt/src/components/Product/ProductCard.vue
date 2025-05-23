<!-- src/components/ProductCard.vue -->
<template>
  <div class="card">
    <div class="card-header">
      <h3 class="bank">{{ product.kor_co_nm }}</h3>
      <h4 class="title">{{ product.fin_prdt_nm }}</h4>
    </div>
    <div class="card-body">
      <div class="rate">
        <span class="label">최고금리</span>
        <span class="value high">{{ product.max_intr_rate }}%</span>
      </div>
      <div class="rate">
        <span class="label">기본금리</span>
        <span class="value base">{{ product.base_intr_rate }}%</span>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  product: Object
})
</script>

<style scoped>
.card {
  border: 1px solid #eee;
  border-radius: 12px;
  padding: 1rem;
  background: #fff;
  box-shadow: 0 4px 10px rgba(0,0,0,0.05);
  transition: 0.3s ease;
}
.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 12px rgba(0,0,0,0.1);
}
.card-header {
  margin-bottom: 1rem;
}
.bank {
  margin: 0;
  color: #2c3e50;
  font-size: 1rem;
}
.title {
  margin: 0.25rem 0;
  font-size: 1.1rem;
  font-weight: bold;
  color: #34495e;
}
.card-body {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
.rate {
  display: flex;
  justify-content: space-between;
  font-weight: 500;
}
.value.high {
  color: #00b894;
}
.value.base {
  color: #636e72;
}
</style>
