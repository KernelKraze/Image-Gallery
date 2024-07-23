<template>
  <div class="gallery-container" :class="{ 'dark-theme': isDarkTheme }">
    <div class="gallery-grid" :style="{ gridTemplateColumns: gridColumns }">
      <transition-group name="fade">
        <div v-for="(item, index) in paginatedMedia" :key="item.id" class="media-item" @click="showMedia(index)">
          <img 
            :src="item.thumb || '/default_thumb.png'" 
            :alt="item.title" 
            loading="lazy" 
            @error="handleImageError($event)"
          >
        </div>
        <!-- Placeholder elements for filling the grid -->
        <div v-for="index in placeholders" :key="'placeholder-' + index" class="media-item placeholder"></div>
      </transition-group>
    </div>
    
    <div class="pagination">
      <button @click="changePage(currentPage - 1)" :disabled="currentPage === 1" class="btn">
        <i class="fas fa-chevron-left"></i> Previous
      </button>
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
      <button @click="changePage(currentPage + 1)" :disabled="currentPage === totalPages" class="btn">
        Next <i class="fas fa-chevron-right"></i>
      </button>
    </div>

    <transition name="modal">
      <div v-if="modalVisible" class="modal" @click.self="closeModal">
        <button class="close btn" @click="closeModal"><i class="fas fa-times"></i></button>
        <div @click="navigate(-1)" class="navigate left btn"><i class="fas fa-chevron-left"></i></div>
        <div @click="navigate(1)" class="navigate right btn"><i class="fas fa-chevron-right"></i></div>
        <div class="modal-content" @click.stop>
          <transition name="fade" mode="out-in">
            <img v-if="currentMedia.type === 'image'" :key="currentMedia.src" :src="currentMedia.src" :alt="currentMedia.title">
            <video v-else-if="currentMedia.type === 'video'" :key="currentMedia.src" :src="currentMedia.src" controls></video>
          </transition>
        </div>
        <div class="danmaku-container">
          <div v-for="(text, index) in visibleDanmaku" :key="'danmaku-' + index" class="danmaku" :style="{ top: text.top + '%', animationDuration: text.duration + 's' }">{{ text.content }}</div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import { ref, computed, onMounted, watch, onUnmounted } from 'vue'

export default {
  setup() {
    // 存储媒体项目的数组
    const mediaData = ref([])
    // 当前页码
    const currentPage = ref(1)
    // 每页显示的项目数量
    const itemsPerPage = ref(15)
    // 模态框是否可见
    const modalVisible = ref(false)
    // 当前显示的媒体项目索引
    const currentMediaIndex = ref(0)
    // 用户输入的页码
    const inputPage = ref(1)
    // 弹幕文本数组
    const danmakuTexts = ref([])
    // 当前可见的弹幕
    const visibleDanmaku = ref([])
    // 是否为暗色主题
    const isDarkTheme = ref(false)
    // 弹幕定时器ID
    const danmakuIntervalId = ref(null)

    // 计算属性：分页后的媒体项目
    const paginatedMedia = computed(() => {
      const start = (currentPage.value - 1) * itemsPerPage.value
      const end = start + itemsPerPage.value
      return mediaData.value.slice(start, end)
    })

    // 计算属性：总页数
    const totalPages = computed(() => Math.ceil(mediaData.value.length / itemsPerPage.value))

    // 计算属性：当前显示的媒体项目
    const currentMedia = computed(() => mediaData.value[currentMediaIndex.value] || {})

    // 计算属性：网格列的样式
    const gridColumns = computed(() => {
      const columnWidth = 200 // 最小列宽
      return `repeat(auto-fit, minmax(${columnWidth}px, 1fr))`
    })

    // 计算属性：需要的占位符数量
    const placeholders = computed(() => {
      const totalItems = paginatedMedia.value.length
      const remainingItems = itemsPerPage.value - totalItems
      return remainingItems > 0 ? remainingItems : 0
    })

    // 从JSON文件获取媒体数据
    const fetchMediaData = async () => {
      try {
        console.log("Fetching media data...")
        const response = await fetch('/media.json')
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`)
        }
        const data = await response.json()
        mediaData.value = data.media.map((item, index) => ({ ...item, id: index }))
        console.log("Media data fetched successfully:", mediaData.value)
      } catch (error) {
        console.error('Error fetching media data:', error)
      }
    }

    // 显示选中的媒体项目
    const showMedia = (index) => {
      currentMediaIndex.value = index + (currentPage.value - 1) * itemsPerPage.value
      modalVisible.value = true
      startDanmaku()
    }

    // 关闭模态框
    const closeModal = () => {
      modalVisible.value = false
      stopDanmaku()
    }

    // 在媒体项目间导航
    const navigate = (direction) => {
      currentMediaIndex.value = (currentMediaIndex.value + direction + mediaData.value.length) % mediaData.value.length
    }

    // 切换到指定页面
    const changePage = (page) => {
      if (page >= 1 && page <= totalPages.value) {
        currentPage.value = page
        inputPage.value = page
      }
    }

    // 跳转到用户指定的页面
    const goToPage = () => {
      const page = inputPage.value
      if (page >= 1 && page <= totalPages.value) {
        currentPage.value = page
      } else {
        inputPage.value = currentPage.value
      }
    }

    // 处理图片加载错误
    const handleImageError = (event) => {
      event.target.src = '/default_thumb.png'
    }

    // 从JSON文件获取弹幕文本
    const fetchDanmakuText = async () => {
      try {
        console.log("Fetching danmaku text...")
        const response = await fetch('/text.json')
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`)
        }
        const data = await response.json()
        danmakuTexts.value = data.danmaku
        console.log("Danmaku text fetched successfully:", danmakuTexts.value)
      } catch (error) {
        console.error('Error fetching danmaku text:', error)
      }
    }

    // 开始显示弹幕
    // 开始显示弹幕
    const startDanmaku = () => {
      if (danmakuTexts.value.length) {
        danmakuIntervalId.value = setInterval(() => {
          const randomIndex = Math.floor(Math.random() * danmakuTexts.value.length)
          const text = danmakuTexts.value[randomIndex]
          visibleDanmaku.value.push({
            content: text,
            top: Math.random() * 80 + 10, // 10% to 90% of the screen height
            duration: Math.random() * 5 + 5 // 5 to 10 seconds
          })
          // 移除已经消失的弹幕
          visibleDanmaku.value = visibleDanmaku.value.filter(d => d.duration > 0)
        }, 1000) // 每秒添加一个新弹幕
      }
    }

    // 停止弹幕
    const stopDanmaku = () => {
      if (danmakuIntervalId.value) {
        clearInterval(danmakuIntervalId.value)
        danmakuIntervalId.value = null
      }
      visibleDanmaku.value = []
    }
    // 检测系统主题并设置
    const checkSystemTheme = () => {
      if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        isDarkTheme.value = true
      }
    }

    // 监听系统主题变化
    const watchSystemTheme = () => {
      if (window.matchMedia) {
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', event => {
          isDarkTheme.value = event.matches
        })
      }
    }

    // 组件挂载时执行
    onMounted(() => {
      fetchMediaData()
      fetchDanmakuText()
      checkSystemTheme()
      watchSystemTheme()
      
      // 添加键盘事件监听器
      window.addEventListener('keydown', handleKeyDown)
    })

    // 组件卸载时执行
    onUnmounted(() => {
      stopDanmaku()
      // 移除键盘事件监听器
      window.removeEventListener('keydown', handleKeyDown)
    })

    // 处理键盘事件
    const handleKeyDown = (event) => {
      if (modalVisible.value) {
        if (event.key === 'ArrowLeft') {
          navigate(-1)
        } else if (event.key === 'ArrowRight') {
          navigate(1)
        } else if (event.key === 'Escape') {
          closeModal()
        }
      }
    }

    // 监听当前页面变化，更新输入框页码
    watch(currentPage, (newPage) => {
      inputPage.value = newPage
    })

    return {
      paginatedMedia,
      totalPages,
      currentMedia,
      currentPage,
      modalVisible,
      inputPage,
      gridColumns,
      placeholders,
      visibleDanmaku,
      isDarkTheme,
      showMedia,
      closeModal,
      navigate,
      changePage,
      goToPage,
      handleImageError,
      danmakuIntervalId
    }
  }
}
</script>

<style scoped>
.gallery-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  background-color: #ffffff;
  color: #000000;
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.dark-theme {
  background-color: #121212;
  color: #ffffff;
}

.gallery-grid {
  display: grid;
  gap: 20px;
  margin-bottom: 20px;
  width: 100%;
}

.media-item {
  position: relative;
  overflow: hidden;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
  aspect-ratio: 1 / 1;
}

.media-item::before {
  content: '';
  display: block;
  padding-top: 100%;
}

.media-item img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.media-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.media-item:hover img {
  transform: scale(1.05);
}

.media-item.placeholder {
  background-color: #f0f0f0;
  border: 1px dashed #cccccc;
}

.dark-theme .media-item.placeholder {
  background-color: #1e1e1e;
  border: 1px dashed #3f3f3f;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
  background-color: rgba(255, 255, 255, 0.8);
  padding: 10px;
  border-radius: 10px;
  backdrop-filter: blur(5px);
  transition: background-color 0.3s ease;
}

.dark-theme .pagination {
  background-color: rgba(18, 18, 18, 0.8);
}

.page-input {
  display: flex;
  align-items: center;
  margin: 0 10px;
}

.page-input input {
  width: 50px;
  padding: 5px;
  border: 1px solid #cccccc;
  border-radius: 4px;
  text-align: center;
  font-size: 16px;
  background-color: #ffffff;
  color: #000000;
  transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
}

.dark-theme .page-input input {
  border-color: #3f3f3f;
  background-color: #1e1e1e;
  color: #ffffff;
}

.page-input span {
  margin-left: 5px;
}

.btn {
  padding: 10px 20px;
  margin: 0 5px;
  background-color: #3f3f3f;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.1s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.btn:hover:not(:disabled) {
  background-color: #555555;
}

.btn:active:not(:disabled) {
  transform:scale(0.95);
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.9);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  transition: backdrop-filter 0.3s ease;
  backdrop-filter: blur(15px);
}

.modal-content {
  max-width: 90%;
  max-height: 90%;
  position: relative;
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
  font-size: 1.5em;
  background-color: rgba(63, 63, 63, 0.7);
  color: white;
  border: none;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.1s ease;
}

.close:hover,
.navigate:hover {
  background-color: rgba(85, 85, 85, 0.7);
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

.danmaku-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  pointer-events: none;
}

.danmaku {
  position: absolute;
  left: 100%;
  white-space: nowrap;
  color: white;
  font-size: 1.2em;
  background-color: rgba(0, 0, 0, 0.6);
  padding: 5px 10px;
  border-radius: 20px;
  animation: danmaku-scroll linear;
}

@keyframes danmaku-scroll {
  from {
    transform: translateX(0);
  }
  to {
    transform: translateX(-100%);
  }
}

/* Transition animations */
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

/* 添加页面切换动画 */
.fade-move,
.fade-enter-active,
.fade-leave-active {
  transition: all 0.5s cubic-bezier(0.55, 0, 0.1, 1);
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: scaleY(0.01) translate(30px, 0);
}

.fade-leave-active {
  position: absolute;
}

@media (max-width: 768px) {
  .gallery-container {
    padding: 10px;
  }

  .pagination {
    flex-wrap: wrap;
  }

  .btn {
    margin: 5px;
  }
}
</style>