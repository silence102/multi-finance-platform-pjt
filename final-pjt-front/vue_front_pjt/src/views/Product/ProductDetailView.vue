<template>
  <div class="detail-container">
    <div class="card">
      <h2 class="title">{{ product?.fin_prdt_nm }}</h2>
      <p class="subtitle">{{ product?.kor_co_nm }}</p>

      <div class="info" v-if="product">
        <div class="info-item">
          <label>상품 코드</label>
          <span>{{ product.fin_prdt_cd }}</span>
        </div>
        <div class="info-item">
          <label>최고 금리</label>
          <span class="rate">{{ product.max_intr_rate }}%</span>
        </div>
        <div class="info-item">
          <label>기본 금리</label>
          <span class="rate">{{ product.base_intr_rate }}%</span>
        </div>
        <div class="info-item">
          <label>상품 유형</label>
          <span>{{ product.type }}</span>
        </div>
      </div>

      <div v-else class="loading">로딩 중...</div>

      <button class="back-btn" @click="goBack">← 뒤로 가기</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const product = ref(null)

onMounted(async () => {
  const id = route.params.id
//   try {
//     const res = await axios.get(`http://localhost:8000/finlife/deposit-products/${id}/`)
//     product.value = res.data
//   } catch (err) {
//     console.error('데이터 요청 실패:', err)
//   }
  // 👉 임시 더미 데이터
  product.value = {
    fin_prdt_cd: id,
    fin_prdt_nm: '임시 예적금 상품',
    kor_co_nm: '테스트은행',
    max_intr_rate: 3.5,
    base_intr_rate: 2.5,
    type: '예금'
  }
})

function goBack() {
  router.back()
}
</script>

<style scoped>
.detail-container {
  display: flex;
  justify-content: center;
  padding: 3rem 1rem;
  background: #f8f9fa;
  min-height: 100vh;
}

.card {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  max-width: 600px;
  width: 100%;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

.title {
  font-size: 1.8rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
  color: #2c3e50;
}

.subtitle {
  color: #7f8c8d;
  font-size: 1rem;
  margin-bottom: 2rem;
}

.info-item {
  margin-bottom: 1.2rem;
  display: flex;
  justify-content: space-between;
  border-bottom: 1px dashed #ddd;
  padding-bottom: 0.5rem;
}

.info-item label {
  font-weight: bold;
  color: #333;
}

.rate {
  color: #27ae60;
  font-weight: bold;
}

.loading {
  padding: 2rem;
  color: #888;
  text-align: center;
}

.back-btn {
  margin-top: 2rem;
  padding: 10px 16px;
  border: none;
  background-color: #3498db;
  color: white;
  font-weight: bold;
  border-radius: 6px;
  cursor: pointer;
  width: 100%;
  transition: background 0.3s ease;
}

.back-btn:hover {
  background-color: #2980b9;
}
</style>