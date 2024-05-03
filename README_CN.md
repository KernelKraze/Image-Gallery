# 🖼️ 图片画廊项目

欢迎来到图片画廊项目！这个仓库提供了一个在树莓派上展示和管理图片和视频的完整解决方案。

## 📂 项目结构

📁 Project Root

📝 CreateJson.py
🖼️ banner.png
📝 check_thumb.py
📝 create_gallery_pages.py
📷 default_thumb.png
📝 generate_thumbnails.py
🖥️ index.html
📝 media.json
📜 script.js
🎨 wel-come.svg
    📁 .static
        📁 css
            🎨 global.css



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

## 🛠️ 使用指南

1. **创建媒体文件夹**：首先，创建一个用于存放媒体文件的目录。命名格式为 `{number}photo`，其中 `{number}` 代表章节或标识符。

2. **运行脚本**：
   - 运行 `CreateJson.py` 生成包含元数据的 `media.json` 文件。
   - 运行 `generate_thumbnails.py` 为媒体文件创建缩略图。

3. **检查缩略图**：如果你认为可能缺少一些缩略图，运行 `check_thumb.py` 来自动化检查并修复问题。

4. **准备素材**：确保你已经准备好以下素材：
   - `banner.png`
   - `default_thumb.png`
   - `wel-come.svg`

   或者，你可以手动调整源代码以自定义这些素材。


## 📜 许可证

本项目采用 MIT 许可证。详情请参阅 [LICENSE](LICENSE) 文件。
