<template>
    <div class="home-container">
        <h1 class="main-title">🎬 MyTube에 오신 걸 환영합니다</h1>
        <p class="intro-text">
            YouTube 영상을 검색하고, 마음에 드는 영상을 저장해두고, <br>
            나중에 다시 확인할 수 있는 간단하고 편리한 영상 큐레이션 서비스입니다.
        </p>

        <ul class="feature-list">
            <li>🔍 유튜브 영상 검색</li>
            <li>📄 상세 정보 확인</li>
            <li>📌 마음에 드는 영상 저장</li>
            <li>🕒 나중에 볼 영상 목록 관리</li>
        </ul>

        <router-link to="/search" class="search-button">지금 영상 검색하기</router-link>
    </div>
</template>

<style scoped>
.home-container {
    max-width: 900px;
    margin: 80px auto;
    padding: 20px;
    text-align: center;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.main-title {
    font-size: 32px;
    margin-bottom: 20px;
    color: #333;
}

.intro-text {
    font-size: 18px;
    margin-bottom: 30px;
    color: #555;
    line-height: 1.6;
}

.feature-list {
    list-style: none;
    padding: 0;
    margin-bottom: 40px;
}

.feature-list li {
    font-size: 16px;
    margin: 10px 0;
}

.search-button {
    display: inline-block;
    padding: 12px 24px;
    font-size: 16px;
    background-color: #ff2e63;
    color: white;
    border-radius: 6px;
    text-decoration: none;
    transition: background-color 0.2s ease;
}

.search-button:hover {
    background-color: #ff2e63;
}
</style>
