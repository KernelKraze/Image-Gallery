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

    fetch('./media.json')
        .then(response => response.json())
        .then(data => {
            mediaData = data.media;
            mediaData.forEach((item, index) => {
                let thumbElement = document.createElement('img');
                thumbElement.src = item.thumb || './default_thumb.png'; // 使用缩略图
                thumbElement.classList.add('media');
                thumbElement.alt = 'Gallery Media';
                thumbElement.loading = "lazy";
                thumbElement.onerror = () => {
                    thumbElement.src = './default_thumb.png';
                };
                thumbElement.onclick = () => showMedia(index);
                gallery.appendChild(thumbElement);
            });
        });

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
            fullMedia.src = item.src; // 现在才加载视频源
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

    spanClose.onclick = () => {
        modal.style.display = "none";
        if (currentMedia && currentMedia.tagName === 'VIDEO') {
            currentMedia.pause();
        }
    };
    navLeft.onclick = () => {
        currentIndex = (currentIndex - 1 + mediaData.length) % mediaData.length;
        showMedia(currentIndex);
    };
    navRight.onclick = () => {
        currentIndex = (currentIndex + 1) % mediaData.length;
        showMedia(currentIndex);
    };
});
