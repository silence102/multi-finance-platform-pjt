// src/views/ProductView.vue
<template>
  <div class="container">
    <h2 class="page-title">예적금 상품 비교</h2>

    <!-- 🔍 키워드 검색 + 필터 + 정렬 -->
    <div class="filter-bar">
      <input
        type="text"
        v-model="searchKeyword"
        placeholder="상품명 또는 금융사 검색"
        class="search-input"
      />
      <button
        v-for="type in productTypes"
        :key="type"
        :class="['filter-btn', { active: selectedType === type }]"
        @click="selectedType = type"
      >
        {{ type }}
      </button>
      <select v-model="sortOption" class="sort-select">
        <option value="">정렬 없음</option>
        <option value="max">최고금리순</option>
        <option value="base">기본금리순</option>
      </select>
    </div>

    <div class="product-grid">
      <RouterLink
        v-for="product in filteredProducts"
        :key="product.fin_prdt_cd"
        :to="{ name: 'ProductDetail', params: { id: product.fin_prdt_cd } }"
        class="card-link"
      >
        <ProductCard :product="product" />
      </RouterLink>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { RouterLink } from 'vue-router'
import ProductCard from '@/components/Product/ProductCard.vue'

const products = ref([
  {
    fin_prdt_cd: '1011010010001',
    fin_prdt_nm: 'BNK더조은정기예금',
    kor_co_nm: '경남은행',
    max_intr_rate: 3.55,
    base_intr_rate: 3.05,
    type: '예금'
  },
  {
    fin_prdt_cd: '1022020010001',
    fin_prdt_nm: 'Sh첫만남우대예금',
    kor_co_nm: '수협은행',
    max_intr_rate: 3.6,
    base_intr_rate: 2.55,
    type: '예금'
  },
  {
    fin_prdt_cd: '1033030010001',
    fin_prdt_nm: 'i-ONE놀이터예금',
    kor_co_nm: '기업은행',
    max_intr_rate: 3.55,
    base_intr_rate: 3.25,
    type: '예금'
  },
  {
    fin_prdt_cd: '1044040010001',
    fin_prdt_nm: '카카오뱅크 26주 적금',
    kor_co_nm: '카카오뱅크',
    max_intr_rate: 4.0,
    base_intr_rate: 2.0,
    type: '적금'
  },
  {
    fin_prdt_cd: '1055050010001',
    fin_prdt_nm: '롯데자이언츠 예적금',
    kor_co_nm: '롯데은행',
    max_intr_rate: 3.8,
    base_intr_rate: 3.1,
    type: '적금'
  }
])

const productTypes = ['전체', '예금', '적금']
const selectedType = ref('전체')
const searchKeyword = ref('')
const sortOption = ref('')

const filteredProducts = computed(() => {
  let list = products.value
  if (selectedType.value !== '전체') {
    list = list.filter(p => p.type === selectedType.value)
  }
  if (searchKeyword.value.trim()) {
    const keyword = searchKeyword.value.toLowerCase()
    list = list.filter(p =>
      p.fin_prdt_nm.toLowerCase().includes(keyword) ||
      p.kor_co_nm.toLowerCase().includes(keyword)
    )
  }
  if (sortOption.value === 'max') {
    list = [...list].sort((a, b) => b.max_intr_rate - a.max_intr_rate)
  } else if (sortOption.value === 'base') {
    list = [...list].sort((a, b) => b.base_intr_rate - a.base_intr_rate)
  }
  return list
})
</script>

<style scoped>
.container {
  padding: 2rem;
}
.page-title {
  font-size: 1.8rem;
  font-weight: bold;
  margin-bottom: 1rem;
}
.filter-bar {
  margin-bottom: 1.5rem;
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
  align-items: center;
}
.search-input {
  padding: 8px 12px;
  font-size: 0.95rem;
  border: 1px solid #ccc;
  border-radius: 6px;
  min-width: 220px;
}
.filter-btn {
  padding: 6px 14px;
  border: 1px solid #ccc;
  border-radius: 20px;
  background: white;
  cursor: pointer;
  font-size: 0.95rem;
}
.filter-btn.active {
  background: #2d98da;
  color: white;
  font-weight: bold;
  border-color: #2d98da;
}
.sort-select {
  padding: 6px 10px;
  font-size: 0.95rem;
  border-radius: 6px;
  border: 1px solid #ccc;
}
.card-link {
  text-decoration: none;
  color: inherit;
}
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}
</style>
