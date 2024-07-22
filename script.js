document.addEventListener("DOMContentLoaded", function () {
    const gallery = document.getElementById('imageGallery');
    const modal = document.getElementById('myModal');
    const modalContent = document.getElementById('modalContent');
    const spanClose = document.querySelector(".close");
    const navLeft = document.querySelector(".navigate.left");
    const navRight = document.querySelector(".navigate.right");
    let currentIndex = 0;
    let mediaData = [];
    let currentMedia = null;

    function fetchMediaData() {
        return fetch('./media.json')
            .then(response => response.json())
            .then(data => {
                mediaData = data.media;
                return mediaData;
            });
    }

    function createMediaElement(item, index) {
        let thumbElement = document.createElement('img');
        thumbElement.src = item.thumb || './default_thumb.png';
        thumbElement.classList.add('media');
        thumbElement.alt = 'Gallery Media';
        thumbElement.loading = "lazy";
        thumbElement.onerror = () => {
            thumbElement.src = './default_thumb.png';
        };
        thumbElement.onclick = () => showMedia(index);
        return thumbElement;
    }

    function showMedia(index) {
        if (currentMedia && currentMedia.tagName === 'VIDEO') {
            currentMedia.pause();
        }
        modal.style.display = "block";
        modalContent.innerHTML = '';
        let item = mediaData[index];
        let fullMedia;
        if (item.type === 'video') {
            fullMedia = document.createElement('video');
            fullMedia.src = item.src;
            fullMedia.controls = true;
            fullMedia.loop = true;
        } else {
            fullMedia = document.createElement('img');
            fullMedia.src = item.src;
        }
        fullMedia.loading = "lazy";
        modalContent.appendChild(fullMedia);
        currentIndex = index;
        currentMedia = fullMedia;
    }

    function closeModal() {
        modal.style.display = "none";
        if (currentMedia && currentMedia.tagName === 'VIDEO') {
            currentMedia.pause();
        }
    }

    function navigateMedia(direction) {
        currentIndex = (currentIndex + direction + mediaData.length) % mediaData.length;
        showMedia(currentIndex);
    }

    fetchMediaData().then(mediaData => {
        mediaData.forEach((item, index) => {
            gallery.appendChild(createMediaElement(item, index));
        });
    });

    spanClose.onclick = closeModal;
    navLeft.onclick = () => navigateMedia(-1);
    navRight.onclick = () => navigateMedia(1);

    document.addEventListener('keydown', function(event) {
        if (modal.style.display === "block") {
            switch(event.key) {
                case "ArrowLeft":
                    navigateMedia(-1);
                    break;
                case "ArrowRight":
                    navigateMedia(1);
                    break;
                case "Escape":
                    closeModal();
                    break;
            }
        }
    });
});
