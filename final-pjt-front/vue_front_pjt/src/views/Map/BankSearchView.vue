<template>
  <div class="bank-search">
    <header class="header">PJT07 - 은행 검색 애플리케이션</header>
    <div class="container">
      <div class="sidebar">
        <form @submit.prevent="onSearch">
          <label>광역시 / 도</label>
          <select v-model="selectedRegion" @change="onRegionChange">
            <option>광역시 / 도를 선택하세요</option>
            <option v-for="region in mapData.mapInfo" :key="region.name" :value="region.name">
              {{ region.name }}
            </option>
          </select>
          <label>시 / 군 / 구</label>
          <select v-model="selectedDistrict">
            <option>시 / 군 / 구를 선택하세요</option>
            <option v-for="district in filteredDistricts" :key="district">
              {{ district }}
            </option>
          </select>
          <label>은행</label>
          <select v-model="selectedBank">
            <option>은행을 선택하세요</option>
            <option v-for="bank in mapData.bankInfo" :key="bank">
              {{ bank }}
            </option>
          </select>
          <button id="button" type="submit">찾기</button>
          <button id="clear-button" type="button" @click="onClear">지우기</button>
        </form>
        <div id="result-list">
          <div
            v-for="(item, index) in resultList"
            :key="index"
            class="result-item"
            @click="item.onClick"
          >
            <strong>{{ index + 1 }}. {{ item.name }}</strong><br />
            📍 {{ item.address }}<br />
            ☎️ {{ item.phone || '전화번호 없음' }}<br />
            🚗 예상시간: {{ item.duration }}분 / {{ item.distance }}km
          </div>
        </div>
      </div>
      <div id="map">
        <div id="search-message" v-if="searchMessage">{{ searchMessage }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
const JS_KEY = import.meta.env.VITE_KAKAO_JS_KEY
const REST_KEY = import.meta.env.VITE_KAKAO_REST_KEY
const MOBILITY_KEY = import.meta.env.VITE_KAKAO_MOBILITY_KEY

async function getKeywordSearch(keyword) {
  const res = await fetch(`https://dapi.kakao.com/v2/local/search/keyword.json?query=${encodeURIComponent(keyword)}`, {
    headers: { Authorization: `KakaoAK ${REST_KEY}` }
  })
  return (await res.json()).documents
}

async function getDirections(originX, originY, destX, destY) {
  const res = await fetch(`https://apis-navi.kakaomobility.com/v1/directions?origin=${originX},${originY}&destination=${destX},${destY}`, {
    headers: { Authorization: `KakaoAK ${MOBILITY_KEY}` }
  })
  return await res.json()
}

const originLat = 37.5012743
const originLng = 127.039585

const selectedRegion = ref('')
const selectedDistrict = ref('')
const selectedBank = ref('')
const mapData = ref({ mapInfo: [], bankInfo: [] })
const resultList = ref([])
const searchMessage = ref('')
const map = ref(null)
const markers = ref([])
const polylines = ref([])
const openInfoWindow = ref(null)

const filteredDistricts = computed(() => {
  const region = mapData.value.mapInfo.find(r => r.name === selectedRegion.value)
  return region ? region.countries : []
})

const onRegionChange = () => {
  selectedDistrict.value = ''
}

onMounted(async () => {
  console.log('kakao:', window.kakao)
  const res = await fetch('/data.json')
  const data = await res.json()
  mapData.value = data

  if (window.kakao && window.kakao.maps) {
    initMap()
  } else {
    const script = document.createElement('script')
    script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${JS_KEY}&autoload=false&libraries=services`
    script.onload = () => {
      window.kakao.maps.load(() => {
        initMap()
      })
    }
    document.head.appendChild(script)
  }
})

function initMap() {
  const container = document.getElementById('map')
  map.value = new kakao.maps.Map(container, {
    center: new kakao.maps.LatLng(originLat, originLng),
    level: 5
  })
}

function onClear() {
  selectedRegion.value = ''
  selectedDistrict.value = ''
  selectedBank.value = ''
  resultList.value = []
  searchMessage.value = ''
  clearMap()
}

function clearMap() {
  markers.value.forEach(m => m.setMap(null))
  polylines.value.forEach(p => p.setMap(null))
  if (openInfoWindow.value) openInfoWindow.value.close()
  markers.value = []
  polylines.value = []
  openInfoWindow.value = null
}

const onSearch = async () => {
  clearMap()
  searchMessage.value = '검색 중입니다...'

  const region = selectedRegion.value
  const district = selectedDistrict.value
  const bank = selectedBank.value

  if ([region, district, bank].some(v => v.includes('선택'))) {
    alert('모든 항목을 선택하세요.')
    searchMessage.value = ''
    return
  }

  const keyword = `${region} ${district} ${bank}`
  const places = await getKeywordSearch(keyword)
  if (!places.length) {
    searchMessage.value = '해당 지역에 은행 지점을 찾을 수 없습니다.'
    return
  }

  // 출발지 마커 생성
  const originMarker = new kakao.maps.Marker({
    map: map.value,
    position: new kakao.maps.LatLng(originLat, originLng),
    zIndex: 10,
    title: '출발지'
  })
  markers.value.push(originMarker)

  resultList.value = []

  // 결과 마커 + 리스트
  for (let i = 0; i < places.length; i++) {
    const place = places[i]

    const marker = new kakao.maps.Marker({
      map: map.value,
      position: new kakao.maps.LatLng(place.y, place.x)
    })
    markers.value.push(marker)

    const showRoute = async () => {
      if (openInfoWindow.value) openInfoWindow.value.close()
      polylines.value.forEach(p => p.setMap(null))
      polylines.value = []

      const result = await getDirections(originLng, originLat, place.x, place.y)
      const summary = result.routes?.[0]?.summary
      const distanceKm = summary ? (summary.distance / 1000).toFixed(2) : '-'
      const durationMin = summary ? Math.round(summary.duration / 60) : '-'

      const info = new kakao.maps.InfoWindow({
        content: `<div style="padding:12px;">🏦 ${place.place_name}<br/>🚗 ${durationMin}분 / ${distanceKm}km</div>`
      })
      info.open(map.value, marker)
      openInfoWindow.value = info

      const path = result.routes[0].sections[0].roads.flatMap(road =>
        road.vertexes.reduce((acc, val, i, arr) => {
          if (i % 2 === 0) acc.push(new kakao.maps.LatLng(arr[i + 1], val))
          return acc
        }, [])
      )

      const polyline = new kakao.maps.Polyline({
        path,
        strokeWeight: 4,
        strokeColor: '#007aff',
        strokeOpacity: 0.9
      })
      polyline.setMap(map.value)
      polylines.value.push(polyline)
    }

    kakao.maps.event.addListener(marker, 'click', showRoute)

    resultList.value.push({
      name: place.place_name,
      address: place.address_name,
      phone: place.phone,
      distance: '-', // 추후 개선 가능
      duration: '-',
      onClick: showRoute
    })
  }

  searchMessage.value = '출력된 마커를 클릭하거나, 리스트를 선택하세요.'
  setTimeout(() => {
    searchMessage.value = ''
  }, 4000)
}

</script>

<style scoped>
.bank-search {
  font-family: Arial, sans-serif;
}
.header {
  background-color: #e17055;
  color: white;
  padding: 15px;
  text-align: center;
  font-size: 20px;
  font-weight: bold;
}
.container {
  display: flex;
}
.sidebar {
  width: 320px;
  padding: 20px;
  background: #f9f9f9;
  border-right: 1px solid #ddd;
}
.sidebar select,
.sidebar button {
  width: 100%;
  margin-bottom: 12px;
  padding: 8px;
  font-size: 14px;
}
#map {
  flex-grow: 1;
  height: 700px;
  position: relative;
  background-color: #eaeaea;
}
#search-message {
  position: absolute;
  top: 10px;
  left: 50%;
  transform: translateX(-50%);
  background: #fff3e0;
  color: #e17055;
  padding: 10px 16px;
  border-radius: 6px;
  border: 1px solid #e17055;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  font-size: 14px;
  font-weight: bold;
  z-index: 10;
}
.result-item {
  padding: 6px 10px;
  margin-bottom: 6px;
  border-radius: 4px;
  cursor: pointer;
  border: 1px solid #ddd;
  background: white;
}
.result-item:hover {
  background: #ffece5;
  border-color: #e17055;
}
#button {
  background-color: #e17055;
  color: white;
  font-weight: bold;
}
#clear-button {
  background: #ccc;
  color: #333;
  font-weight: bold;
}
</style>
