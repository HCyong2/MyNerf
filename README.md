# MyNerf

## 简介

使用Nerf构建了自己的物体重建，提供了一些小工具。

原始图片

<center>
    <img style="width:50%" src=".\data\nerf_llff_data\MyPictures\images\miku06_41.jpg"/>
</center>

图片8倍采样下的训练重建效果

<center>
    <img style="width:50%" src=".\gif\video.gif"/>
</center>

图片4倍采样下的训练重建效果(分辨率高，但噪音多)

<center>
    <img style="width:50%" src=".\gif\video_failure.gif"/>
</center>

## 内容目录

```bash
data                                # 原始图片和相机参数
gif                                 # 结果
downsample.py                       # 图片下采样
run_nerf.py                         # 修改后的run_nerf代码
Video_to_frame.py                   # 将视频抽帧成图片
```

## 使用说明

本仓库仅仅只提供了一些用于构建自己图片数据集的工具，请配合Nerf官方代码使用：

[ A PyTorch implementation of NeRF (github.com)](https://github.com/yenchenlin/nerf-pytorch)

具体训练过程请参考 Nerf 教程

Video_to_frame.py 提供了从连续的视频中抽取图片的功能，设置帧数间隔以抽取不同数量的图片

downsample.py      提供了让图片下采样的功能，虽然Nerf也集成了下采样功能，但我运行时出现报错。

run_nerf.py            在源代码基础上添加了tensorboard记录，可以观察训练集和测试集上的loss曲线和psnr曲线