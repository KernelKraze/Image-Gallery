<template>
  <div>
    <transition-group name="gallery" tag="div" class="gallery">
      <div v-for="(item, index) in paginatedMedia" :key="item.id" class="media-item" @click="showMedia(index)">
        <img 
          :src="item.thumb || '/default_thumb.png'" 
          :alt="item.title" 
          loading="lazy" 
          @error="handleImageError($event)"
        >
      </div>
    </transition-group>
    
    <div class="pagination">
      <button @click="changePage(currentPage - 1)" :disabled="currentPage === 1" class="btn-animate">Previous</button>
      <div class="page-input">
        <input 
          v-model.number="inputPage" 
          @keyup.enter="goToPage"
          type="number" 
          min="1" 
          :max="totalPages"
        >
        <span>/ {{ totalPages }}</span>
      </div>
      <button @click="changePage(currentPage + 1)" :disabled="currentPage === totalPages" class="btn-animate">Next</button>
    </div>

    <transition name="modal">
      <div v-if="modalVisible" class="modal" @click.self="closeModal">
        <span class="close btn-animate" @click="closeModal"><i class="fas fa-times"></i></span>
        <span class="navigate left btn-animate" @click="navigate(-1)"><i class="fas fa-chevron-left"></i></span>
        <span class="navigate right btn-animate" @click="navigate(1)"><i class="fas fa-chevron-right"></i></span>
        <div class="modal-content">
          <transition name="fade" mode="out-in">
            <img v-if="currentMedia.type === 'image'" :key="currentMedia.src" :src="currentMedia.src" :alt="currentMedia.title">
            <video v-else-if="currentMedia.type === 'video'" :key="currentMedia.src" :src="currentMedia.src" controls></video>
          </transition>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import { ref, computed, onMounted, watch } from 'vue'

export default {
  setup() {
    const mediaData = ref([])
    const currentPage = ref(1)
    const itemsPerPage = 12
    const modalVisible = ref(false)
    const currentMediaIndex = ref(0)
    const inputPage = ref(1)

    const paginatedMedia = computed(() => {
      const start = (currentPage.value - 1) * itemsPerPage
      const end = start + itemsPerPage
      return mediaData.value.slice(start, end)
    })

    const totalPages = computed(() => Math.ceil(mediaData.value.length / itemsPerPage))

    const currentMedia = computed(() => mediaData.value[currentMediaIndex.value] || {})

    const fetchMediaData = async () => {
      try {
        const response = await fetch('/media.json')
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`)
        }
        const data = await response.json()
        mediaData.value = data.media.map((item, index) => ({ ...item, id: index }))
      } catch (error) {
        console.error('Error fetching media data:', error)
      }
    }

    const showMedia = (index) => {
      currentMediaIndex.value = index + (currentPage.value - 1) * itemsPerPage
      modalVisible.value = true
    }

    const closeModal = () => {
      modalVisible.value = false
    }

    const navigate = (direction) => {
      currentMediaIndex.value = (currentMediaIndex.value + direction + mediaData.value.length) % mediaData.value.length
    }

    const changePage = (page) => {
      if (page >= 1 && page <= totalPages.value) {
        currentPage.value = page
        inputPage.value = page
      }
    }

    const goToPage = () => {
      const page = inputPage.value
      if (page >= 1 && page <= totalPages.value) {
        currentPage.value = page
      } else {
        inputPage.value = currentPage.value
      }
    }

    watch(currentPage, (newPage) => {
      inputPage.value = newPage
    })

    onMounted(fetchMediaData)

    return {
      paginatedMedia,
      totalPages,
      currentMedia,
      currentPage,
      modalVisible,
      inputPage,
      showMedia,
      closeModal,
      navigate,
      changePage,
      goToPage
    }
  }
}
</script>

<style scoped>
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
  padding: 20px;
}

.media-item {
  overflow: hidden;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
}

.media-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.media-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.media-item:hover img {
  transform: scale(1.05);
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}

.page-input {
  display: flex;
  align-items: center;
  margin: 0 10px;
}

.page-input input {
  width: 50px;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
  text-align: center;
  font-size: 16px;
}

.page-input span {
  margin-left: 5px;
}

.btn-animate {
  padding: 10px 20px;
  margin: 0 10px;
  background-color: #262727;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.1s ease;
}

.btn-animate:hover:not(:disabled) {
  background-color: #2980b9;
}

.btn-animate:active:not(:disabled) {
  transform: scale(0.95);
}

.btn-animate:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  max-width: 90%;
  max-height: 90%;
}

.modal-content img,
.modal-content video {
  max-width: 100%;
  max-height: 90vh;
  object-fit: contain;
}

.close,
.navigate {
  position: absolute;
  font-size: 2em;
  color: white;
  cursor: pointer;
  transition: color 0.3s ease, transform 0.1s ease;
}

.close:hover,
.navigate:hover {
  color: #3498db;
}

.close:active,
.navigate:active {
  transform: scale(0.9);
}

.close {
  top: 20px;
  right: 20px;
}

.navigate {
  top: 50%;
  transform: translateY(-50%);
}

.left {
  left: 20px;
}

.right {
  right: 20px;
}

/* Transition animations */
.gallery-enter-active,
.gallery-leave-active {
  transition: all 0.5s ease;
}

.gallery-enter-from,
.gallery-leave-to {
  opacity: 0;
  transform: translateY(30px);
}

.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>