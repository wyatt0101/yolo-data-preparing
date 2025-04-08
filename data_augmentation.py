import os
import cv2
import numpy as np
import albumentations as A
from albumentations.pytorch import ToTensorV2

# 输入/输出文件夹
input_dir = "\Datasets\yolo_datasets_split\\train\images"  # 原始图片路径
label_dir = "\Datasets\yolo_datasets_split\\train\labels"  # 原始标注路径
output_dir = "\Datasets\yolo_datasets_split\dataset_aug\images"  # 增强后图片保存路径
output_label_dir = "\Datasets\yolo_datasets_split\dataset_aug\labels"  # 增强后标注路径

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)
os.makedirs(output_label_dir, exist_ok=True)

# 定义数据增强
augmentations = [
    A.RandomBrightnessContrast(brightness_limit=0.3, contrast_limit=0.3, p=1.0),  # 亮度和对比度
    A.HueSaturationValue(hue_shift_limit=30, sat_shift_limit=30, val_shift_limit=30, p=1.0),  # 色调变化
    A.GaussianBlur(blur_limit=(3, 7), p=1.0),  # 高斯模糊
    A.GaussNoise(var_limit=(10.0, 50.0), p=1.0),  # 高斯噪声
    # A.RandomGamma(gamma_limit=(50, 130), p=1.0)  # Gamma 调整
]

# 遍历数据集
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # 处理图片
        image_path = os.path.join(input_dir, filename)
        label_path = os.path.join(label_dir, filename.replace(".jpg", ".txt").replace(".png", ".txt"))

        # 读取图片
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # OpenCV 读取的是 BGR，转换为 RGB

        # **1. 先保存原始图片**
        original_image_path = os.path.join(output_dir, filename)
        cv2.imwrite(original_image_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

        # **2. 复制原始标签**
        if os.path.exists(label_path):
            with open(label_path, "r") as f:
                label_data = f.readlines()
            with open(os.path.join(output_label_dir, filename.replace(".jpg", ".txt").replace(".png", ".txt")), "w") as f:
                f.writelines(label_data)  # 直接复制 YOLO 标签

        # **3. 进行数据增强**
        for i, aug in enumerate(augmentations):  # 每种增强方式生成一张新图片
            transformed = aug(image=image)
            transformed_image = transformed["image"]

            # 生成新文件名
            new_filename = filename.replace(".jpg", f"_aug{i}.jpg").replace(".png", f"_aug{i}.png")
            new_label_filename = new_filename.replace(".jpg", ".txt").replace(".png", ".txt")

            # 保存增强后的图片
            cv2.imwrite(os.path.join(output_dir, new_filename), cv2.cvtColor(transformed_image, cv2.COLOR_RGB2BGR))

            # 复制对应的 YOLO 标注文件
            with open(os.path.join(output_label_dir, new_label_filename), "w") as f:
                f.writelines(label_data)  # 复制标签

print("数据增强完成！增强后的图片和标签已保存到 dataset_aug 目录。")
