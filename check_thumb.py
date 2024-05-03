import os
import json

# 读取media.json文件
with open('media.json', 'r') as file:
    media_data = json.load(file)

# 定义缩略图目录
thumbnail_dir = './thumbnails'  # 缩略图目录

# 创建缩略图目录
os.makedirs(thumbnail_dir, exist_ok=True)

# 获取媒体文件列表
media_files = [media['src'] for media in media_data['media']]

# 遍历媒体文件列表，并检查是否有对应的缩略图
for media_file in media_files:
    thumbnail_filename = f"thumbnail_{os.path.basename(media_file)}"
    thumbnail_path = os.path.join(thumbnail_dir, thumbnail_filename)
    if not os.path.exists(thumbnail_path):
        print(f"Thumbnail not found for media: {media_file}")
    else:
        print(f"Thumbnail found for media: {media_file}")

