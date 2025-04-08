import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 设置图片和标注文件夹路径
image_folder = r"D:\Learning\Master\Internship\Datasets\yolo_crack_datasets\images"  # 图片文件夹路径
label_folder = r"D:\Learning\Master\Internship\Datasets\yolo_crack_datasets\labels"  # 标注文件夹路径

# 获取所有图片文件（支持 jpg 和 png）
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png'))]

# 遍历每张图片
for image_file in image_files:
    # 获取图像文件的完整路径
    image_path = os.path.join(image_folder, image_file)

    # 加载图片
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 转换为 RGB 格式以供 matplotlib 使用

    # 获取标注文件路径（假设标注文件与图像文件同名，仅扩展名不同）
    label_file = image_file.split('.')[0] + ".txt"
    label_path = os.path.join(label_folder, label_file)

    # 如果标注文件存在
    if os.path.exists(label_path):
        # 读取标注文件并解析（YOLO 格式）
        with open(label_path, 'r') as f:
            annotations = f.readlines()

        # 绘制标注框（根据 YOLO 格式）
        for annotation in annotations:
            # YOLO 格式为：class_id center_x center_y width height (相对坐标)
            parts = annotation.strip().split()
            class_id, center_x, center_y, width, height = map(float, parts)

            # 获取图像的宽度和高度
            img_width, img_height = image.shape[1], image.shape[0]

            # 计算标注框的实际坐标
            x1 = int((center_x - width / 2) * img_width)
            y1 = int((center_y - height / 2) * img_height)
            x2 = int((center_x + width / 2) * img_width)
            y2 = int((center_y + height / 2) * img_height)

            # 绘制矩形框
            cv2.rectangle(image_rgb, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # 使用 matplotlib 显示图片
    plt.figure(figsize=(10, 10))
    plt.imshow(image_rgb)
    plt.title(f"Image: {image_file}")
    plt.axis('off')  # 不显示坐标轴
    plt.show()

