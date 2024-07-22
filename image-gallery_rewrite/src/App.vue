<template>
  <div id="app">
    <header>
      <div class="banner">
        <img src="./assets/wel-come.svg" alt="Welcome Banner" loading="lazy">
        <img src="./assets/banner.png" alt="Welcome Banner" loading="lazy">
      </div>
    </header>
    <main>
      <Gallery />
    </main>
  </div>
</template>

<script>
import Gallery from './components/ImageGallery.vue'

export default {
  name: 'App',
  components: {
    Gallery
  }
}
</script>

<style src="./assets/global.css"></style>