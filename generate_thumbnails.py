import os
import json
import subprocess

# 读取media.json文件
with open('media.json', 'r') as file:
    media_data = json.load(file)

# 定义缩略图目录
thumbnail_dir = './thumbnails'  # 缩略图目录

# 创建缩略图目录
os.makedirs(thumbnail_dir, exist_ok=True)

# 遍历媒体信息
for media in media_data['media']:
    src = media['src']
    # 确定缩略图文件名，确保统一格式为JPEG
    thumbnail_filename = f"thumbnail_{os.path.basename(src)}.jpg"
    # 构造缩略图文件的完整路径
    thumbnail_path = os.path.join(thumbnail_dir, thumbnail_filename)

    # 使用FFmpeg生成缩略图，确保输出为JPEG格式
    subprocess.run(['ffmpeg', '-i', src, '-vf', 'scale=320:-1', '-vframes', '1', thumbnail_path])

    print(f"Thumbnail generated for media: {src}")
    __import__("time").sleep(2)
