import os
import shutil
import random

# 原始数据集路径
dataset_dir = r"\Datasets\yolo_datasets"
images_dir = os.path.join(dataset_dir, "images")
labels_dir = os.path.join(dataset_dir, "labels")

# 新的数据集文件夹路径
new_dataset_dir = r"\Datasets\yolo_crack_datasets_split"

# 目标划分数据集路径
train_dir = os.path.join(new_dataset_dir, "train")
val_dir = os.path.join(new_dataset_dir, "val")

# 创建新数据集文件夹及其子目录
for folder in [train_dir, val_dir]:
    os.makedirs(os.path.join(folder, "images"), exist_ok=True)
    os.makedirs(os.path.join(folder, "labels"), exist_ok=True)

# 获取所有图片文件
image_files = [f for f in os.listdir(images_dir) if f.endswith((".jpg", ".png"))]
random.shuffle(image_files)  # 随机打乱数据

# 计算划分数量
train_size = int(0.9 * len(image_files))
train_images = image_files[:train_size]
val_images = image_files[train_size:]


# 复制文件到新的文件夹
def copy_files(image_list, target_folder):
    for img_file in image_list:
        img_path = os.path.join(images_dir, img_file)
        label_file = os.path.splitext(img_file)[0] + ".txt"
        label_path = os.path.join(labels_dir, label_file)

        # 复制图片
        shutil.copy(img_path, os.path.join(target_folder, "images", img_file))
        # 复制标签（如果存在）
        if os.path.exists(label_path):
            shutil.copy(label_path, os.path.join(target_folder, "labels", label_file))


copy_files(train_images, train_dir)
copy_files(val_images, val_dir)

# 创建 data.yaml 配置文件
yaml_content = f"""train: {train_dir}/images
val: {val_dir}/images

nc: 1
names: ['crack']
"""

with open(os.path.join(new_dataset_dir, "data.yaml"), "w") as f:
    f.write(yaml_content)

print(f"数据集已成功划分并存储在: {new_dataset_dir}")
