# 🖼️ 图片画廊项目

欢迎来到图片画廊项目！这个仓库提供了一个在树莓派上展示和管理图片和视频的完整解决方案。

## 📂 项目结构

📁 Project Root
├── 📝 CreateJson.py
├── 🖼️ banner.png
├── 📝 check_thumb.py
├── 📝 create_gallery_pages.py
├── 📷 default_thumb.png
├── 📝 generate_thumbnails.py
├── 🖥️ index.html
├── 📝 media.json
├── 📜 script.js
├── 🎨 wel-come.svg
└── 📁 .static
    └── 📁 css
        └── 🎨 global.css



## 🚀 快速开始

1. **CreateJson.py**：该脚本扫描媒体目录，根据章节和页面组织媒体文件，并生成包含元数据的 `media.json` 文件。

2. **check_thumb.py**：该脚本检查 `media.json` 中列出的所有媒体文件的缩略图是否存在。

3. **create_gallery_pages.py**：该脚本生成带有分页功能的画廊 HTML 页面。

4. **generate_thumbnails.py**：该脚本使用 FFmpeg 为所有媒体文件创建缩略图。

5. **index.html**：图片画廊的主要入口。

6. **script.js**：用于处理画廊交互的 JavaScript 文件，例如在模态窗口中显示图片或视频。

7. **banner.png** 和 **wel-come.svg**：画廊的横幅图片。

8. **default_thumb.png**：没有特定缩略图的媒体项目的默认缩略图。

9. **.static/css/global.css**：用于样式化画廊的全局 CSS 文件。

## ✨ 功能

- 🖼️ **图片和视频支持**：画廊支持图片和视频。
- 📋 **媒体元数据**：根据文件名模式按章节和页面组织媒体文件。
- 🖼️ **缩略图**：为媒体文件生成并使用缩略图。
- 📃 **HTML 画廊页面**：自动创建分页的 HTML 画廊页面。
- 🎯 **用户友好界面**：具有模态窗口和导航功能的交互式画廊。

## 📌 使用

1. 克隆仓库。
2. 将媒体文件放入相应的目录中。
3. 按照上面提到的顺序运行 Python 脚本来准备画廊。
4. 在浏览器中打开 `index.html` 以查看画廊。

## 📜 许可证

本项目采用 MIT 许可证。详情请参阅 [LICENSE](LICENSE) 文件。
