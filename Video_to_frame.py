"""
Video_to_frame -

Author:霍畅
Date:2024/6/20
"""
import os
import cv2
def extract_images(video_path, output_folder):
    # 获取视频文件名
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    # 新建文件夹
    output_path = os.path.join(output_folder, video_name)
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    # 打开视频
    cap = cv2.VideoCapture(video_path)
    # 设置帧间隔
    frame_interval = int(2)
    # 逐帧提取并保存满足间隔要求的帧
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            if count % frame_interval == 0:
                print(count)
                image_name = os.path.join(output_path, f"{video_name}_{count//frame_interval}.jpg")
                cv2.imwrite(image_name, frame)
            count += 1
        else:
            break
    cap.release()

if __name__ == '__main__':
    video_path = 'F:\COLMAP_demo\miku06.mp4'  # 视频文件路径
    output_folder = './data/nerf_llff_data/MyPictures/images'  # 输出文件夹路径
    extract_images(video_path, output_folder)
