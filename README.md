# 🖼️ Image Gallery Project

Welcome to the Image Gallery project! This repository houses a robust solution for displaying and managing image and video collections on a Raspberry Pi.

## 📂 Project Structure

.
├── CreateJson.py
├── banner.png
├── check_thumb.py
├── create_gallery_pages.py
├── default_thumb.png
├── generate_thumbnails.py
├── index.html
├── media.json
├── script.js
├── wel-come.svg
└── .static
└── css
└── global.css


## 🚀 Getting Started

1. **CreateJson.py**: This script scans the media directory, organizes media files by chapters and pages, and generates a `media.json` file containing the metadata.

2. **check_thumb.py**: This script checks for the existence of thumbnails for all media items listed in `media.json`.

3. **create_gallery_pages.py**: This script generates HTML pages for the gallery, with pagination.

4. **generate_thumbnails.py**: This script creates thumbnail images for all media files using FFmpeg.

5. **index.html**: The main entry point for the image gallery.

6. **script.js**: The JavaScript file that handles gallery interactions, such as displaying images or videos in a modal.

7. **banner.png** & **wel-come.svg**: Banner images for the gallery.

8. **default_thumb.png**: Default thumbnail image for media items without a specific thumbnail.

9. **.static/css/global.css**: The global CSS file for styling the gallery.

## ✨ Features

- 🖼️ **Image and Video Support**: The gallery supports both images and videos.
- 📋 **Media Metadata**: Organizes media files based on filename patterns for chapters and pages.
- 🖼️ **Thumbnails**: Generates and uses thumbnails for media files.
- 📃 **HTML Gallery Pages**: Automatically creates paginated HTML gallery pages.
- 🎯 **User-Friendly Interface**: Interactive gallery with modal and navigation.

## 📌 Usage

1. Clone the repository.
2. Add media files in the proper directories.
3. Run the Python scripts in the order mentioned above to prepare the gallery.
4. Open `index.html` in a web browser to view the gallery.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
