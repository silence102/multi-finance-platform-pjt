import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '@/views/HomeView.vue'
import ProductView from '@/views/Product/ProductView.vue'
import AssetView from '@/views/AssetView.vue'
import SignUpView from '@/views/User/SignUpView.vue'
import LoginView from '@/views/User/LoginView.vue'
import ProfileView from '@/views/User/ProfileView.vue'
import BankSearchView from '@/views/Map/BankSearchView.vue'
// import StockView from '@/views/StockView.vue'
// import BankView from '@/views/BankView.vue'
// import CommunityView from '@/views/CommunityView.vue'
// import ProfileView from '@/views/ProfileView.vue'
import VideoHomeView from '@/views/Video/VideoHomeView.vue'
import SearchView from '@/views/Video/SearchView.vue'
import LaterView from '@/views/Video/LaterView.vue'
import VideoItemDetail from '@/components/Video/VideoItemDetail.vue'
import ChannelView from '@/views/Video/ChannelView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'Home', component: HomeView },
    // --------------- 상품 ------------------------
    {
      path: '/products',
      name: 'Products',
      component: ProductView
    },
    {
      path: '/products/:id',
      name: 'ProductDetail',
      component: () => import('@/views/Product/ProductDetailView.vue')
    },
    {
      path: '/asset',
      name: 'Asset',
      component: AssetView
    },
    { 
      path: '/signup', 
      name: 'Signup', 
      component: SignUpView 
    },
    { 
      path: '/login',
      name: 'Login', 
      component: LoginView
    },
    { 
      path: '/stock', 
      name: 'Stock', 
      component: { template: '<div>관심 종목</div>' } 
    },
    // -------------- 은행 찾기 --------------------
    { 
      path: '/bank', 
      name: 'Bank', 
      component: BankSearchView
    },
    { 
      path: '/community', 
      name: 'Community', 
      component: { template: '<div>커뮤니티</div>' } 
    },

    { 
      path: '/profile', 
      name: 'Profile', 
      component: ProfileView 
    },
    // --------- Video ---------------------
    {
      path: '/video',
      name: 'video',
      component: VideoHomeView,
    },
    {
      path: '/search',
      name: 'search',
      component: SearchView
    },
    {
      path: '/later',
      name: 'later',
      component: LaterView
    },
    {
      path: '/video/:id',
      name: 'videoDetail',
      component: VideoItemDetail
    },
    {
      path: '/channel',
      name: 'channel',
      component: ChannelView
    },
  ],
})

export default router
