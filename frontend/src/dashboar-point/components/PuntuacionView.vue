<script setup lang="ts">

import LogoShotokan from "@/dashboar-point/components/LogoShotokan.vue";
import RefereeIcon from "@/dashboar-point/components/RefereeIcon.vue";
</script>
<template>
  <div class="container">
    <div class="columns is-flex-direction-column">
      <div class="is-full">
        <header class="header header--theme-main header-simple">
          <LogoShotokan></LogoShotokan>
          <h1 class="title is-1">IX COPA MURAYANA PANAMÁ</h1>
          <LogoShotokan></LogoShotokan>
        </header>
      </div>
      <div class="is-flex main--section">
        <div class="is-5 is-flex-grow-2">
          <div class="card card__point">
            <h1 class="title title--big-2">TOTAL</h1>
            <h1 class="title title--big-1">0.0</h1>
          </div>
        </div>
        <div class="is-5 is-flex-grow-2">
          <div class="card card__info card--theme-main">
            <header class="card-header">
              <h1 class="title is-1">LAURA NÚÑEZ</h1>
            </header>
            <div class="card-content">
              <div class="info--player">
                <div class="info--item">
                  <span class="title is-3">Dojo:</span><span class="info--text">Jion Karate Do</span>
                </div>
                <div class="info--item">
                  <span class="title is-3">Edad:</span><span class="info--text">25</span>
                </div>
                <div class="info--item">
                  <span class="title is-3">Cinturon:</span><div class="cinturon is--brown"></div>
                </div>
                <div class="info--item">
                  <span class="title is-3">Competicion:</span><span class="info--text">Kata</span>
                </div>
              </div>
              <div class="is-flex is-justify-content-space-between">
                <div class="mini__card mini__card--theme-main">
                  <div class="mini__card--header">
                    <RefereeIcon></RefereeIcon>
                    <span class="title is-1">1</span>
                  </div>
                  <div class="mini__card--content">
                    <h2 class="title is-1">0.0</h2>
                  </div>
                </div>
                <div class="mini__card mini__card--theme-main">
                  <div class="mini__card--header">
                    <RefereeIcon></RefereeIcon>
                    <span class="title is-1">2</span>
                  </div>
                  <div class="mini__card--content">
                    <h2 class="title is-1">0.0</h2>
                  </div>
                </div>
                <div class="mini__card mini__card--theme-main">
                  <div class="mini__card--header">
                    <RefereeIcon></RefereeIcon>
                    <span class="title is-1">3</span>
                  </div>
                  <div class="mini__card--content">
                    <h2 class="title is-1">0.0</h2>
                  </div>
                </div>
                <div class="mini__card mini__card--theme-main">
                  <div class="mini__card--header">
                    <RefereeIcon></RefereeIcon>
                    <span class="title is-1">4</span>
                  </div>
                  <div class="mini__card--content">
                    <h2 class="title is-1">0.0</h2>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.header {
  text-align: center;
  background-color: #1E2025;
  color: #ffffff;
  padding: 1.5rem 1rem 1rem;
  border-bottom-left-radius: .8rem;
  border-bottom-right-radius: .8rem;
  display: flex;
  align-content: center;
  align-items: center;
  justify-content: space-between;
}

.header .title {
  text-align: center;
  color: #ffffff;
  margin-bottom: 0;
  flex-grow: 1;
}

.title--big-1, .title--big-2 {
  font-weight: bold;
}

.title--big-1 {
  font-size: 18rem;
}

.title--big-2 {
  font-size: 6rem;
}

.card.card__point {
  background-color: #1E2025;
  text-align: center;
  border-radius: .8rem;
  height: 80%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.card.card__info{
  margin-left: 1rem;
  height: 80%;
}

.card__point > * {
  color: #ffffff;
}
.mini__card{
  border-radius: .5rem;
  padding: 1.5rem;
}
.mini__card.mini__card--theme-main{
  background-color: #1E2025;
}
.mini__card--header{
  margin-bottom: .6rem;
}
.mini__card--content .title {
  color: #ffffff;
}
.mini__card--header .title{
  color: #ffffff;
}
.main--section{
  height: 100vh;
  padding-top: 3rem;
  padding-bottom: 3rem;
}
.card--theme-main .card-header{
  background-color: #1E2025;
  padding: 1rem .5rem;
  align-items: center;
  justify-content: center;
}
.card--theme-main .card-header .title{
  color: #ffffff;
  text-align: center;
}
.info--player{
  display: flex;
  flex-direction: column;
}
.info--player .info--item{
  display: flex;
  align-items: center;
  align-content: center;
  margin-bottom: 1.5rem;
}
.info--item .title{
  margin: 0 1rem 0 0;
}
.info--item .info--text{
  font-size: 2rem;
}
.cinturon{
  width: 12rem;
  /*height: 1.7rem;*/
  height: 1.8rem;
  background: #ffffff;
  margin: 0;
  border-radius: .3rem;
  border: 1px solid #aaaaaa;
}
</style>