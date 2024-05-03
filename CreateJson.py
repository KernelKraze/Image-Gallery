import os
import json
import re

def parse_filename(filename):
    # 解析文件名以提取数字，如 '1241_p2.jpg'
    match = re.match(r"(\d+)_p(\d+)", filename)
    if match:
        return int(match.group(1)), int(match.group(2))  # 返回章节和页码数字
    return (0, 0)  # 如果没有匹配，返回默认值

def create_or_update_media_list_json(directory, data, path_prefix=""):
    # 定义图片和视频的文件扩展名
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    video_extensions = ['.webm', '.mp4', '.avi']

    # 获取指定目录中的文件和目录列表
    contents = os.listdir(directory)

    # 按章节和页码排序文件
    contents.sort(key=lambda x: parse_filename(x))

    # 更新媒体列表
    for item in contents:
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            # 如果条目是目录，则递归调用 create_or_update_media_list_json
            create_or_update_media_list_json(item_path, data, os.path.join(path_prefix, item))
        else:
            file_extension = os.path.splitext(item)[1].lower()
            if file_extension in image_extensions or file_extension in video_extensions:
                media_type = "video" if file_extension in video_extensions else "image"
                # 使用用户指定的路径前缀构建相对路径
                relative_file_path = os.path.join(path_prefix, item)
                thumbnail_path = os.path.join("thumbnails", f"thumbnail_{os.path.basename(item)}.jpg")
                if not any(media['src'] == relative_file_path for media in data['media']):
                    data['media'].append({
                        "type": media_type, 
                        "src": relative_file_path,
                        "thumb": thumbnail_path  # 添加缩略图路径
                    })

def main():
    base_dir = os.path.dirname(__file__)
    json_filename = 'media.json'
    data = {"media": []}

    # 从基础目录开始递归遍历目录
    for root, dirs, files in os.walk(base_dir):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if re.match(r'\d+photo', folder):
                path_prefix = os.path.relpath(folder_path, base_dir)  # 动态构建路径前缀
                create_or_update_media_list_json(folder_path, data, path_prefix)

    # 将收集的数据写入单个 JSON 文件
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    main()

