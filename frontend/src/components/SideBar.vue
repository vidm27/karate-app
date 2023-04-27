<script setup lang="ts">
import IconFederación from "@/components/IconFederación.vue";

</script>
<template>
  <aside class="aside aside--is-expanded">
    <div class="aside--brand">
      <div class="brand brand--text">
        <IconFederación></IconFederación>
      </div>
    </div>
    <div class="menu menu--main">
      <p class="menu-label">Competencias</p>
      <ul class="menu-list">
        <li class="menu-item">
          <a href="#" class="item">
            <span class="item--text">Kata individual</span>
          </a>
        </li>
        <li class="menu-item">
          <a href="#" class="item">
            <span class="item--text">Sambon</span>
          </a>
        </li>
        <li class="menu-item">
          <a href="#" class="item">
            <span class="item--text">Kumite</span>
          </a>
        </li>
      </ul>
    </div>
  </aside>
</template>


<style scoped>

.aside {
  position: fixed;
  top: 0;
  z-index: 40;
  height: 100vh;
  width: 15rem;
  background: #1e2025;
  transition-property: all;
  transition-timing-function: cubic-bezier(.4, 0, .2, 1);
  transition-duration: 150ms;
  display: flex;
  flex-direction: column;
}

.aside .aside--brand {
  text-transform: capitalize;
  color: #ffffff;
  font-weight: bolder;
  text-align: center;
  font-size: 1.2rem;
  padding-top: .5rem;
  padding-bottom: .5rem;
}

.aside .menu.menu--main {
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  align-items: center;
  flex-grow: 1;
}

.menu.menu--main .menu-label {
  width: 100%;
  text-transform: uppercase;
  font-size: .9rem;
  color: rgb(156, 163, 175);
  padding-left: 1rem;
  padding-right: 1rem;
  margin-top: .6rem;
  margin-bottom: .6rem;
}

.menu-list {
  width: 100%;
}

.menu.menu--main .menu-list .menu-item {
  color: rgb(209, 213, 219);

}

.menu-item .item {
  color: inherit;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: .5em 1rem;
}

.menu-item .item:hover {
  background: #374151;
  color: #ffffff;
  transition: ease all .3s;
}

.item .item--text {
  flex-grow: 1;
  font-size: 1.5rem;
}
</style>