"""
downsample -

Author:霍畅
Date:2024/6/21
"""
import os
from PIL import Image


def downsample_image(input_path, output_path, factor):
    # 打开图像文件
    with Image.open(input_path) as img:
        # 获取原始图像尺寸
        original_size = img.size
        print(f"Original size: {original_size}")

        # 计算下采样后的尺寸
        new_size = (original_size[0] // factor, original_size[1] // factor)
        print(f"New size: {new_size}")

        # 下采样图像
        downsampled_img = img.resize(new_size, Image.LANCZOS)

        # 保存下采样后的图像
        downsampled_img.save(output_path)
        print(f"Downsampled image saved to: {output_path}")


def downsample_images_in_folder(folder_path, factor):
    # 创建输出文件夹路径
    output_folder = os.path.join(os.path.dirname(folder_path), f'images_{factor}')
    os.makedirs(output_folder, exist_ok=True)

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        input_path = os.path.join(folder_path, filename)

        # 仅处理图像文件
        if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            output_path = os.path.join(output_folder, filename)
            downsample_image(input_path, output_path, factor)


# 示例使用
input_folder_path = 'data/nerf_llff_data/MyPictures/images'
downsampling_factor = 4

downsample_images_in_folder(input_folder_path, downsampling_factor)
