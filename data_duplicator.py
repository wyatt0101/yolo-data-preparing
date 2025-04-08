import os
import shutil

# 设置标注文件、图像文件和目标文件夹的路径
label_folder = r"D:\Learning\Master\Internship\Datasets\yolo_crack_datasets\labels"  # 请替换成你的标注文件夹路径
image_folder = r"D:\Learning\Master\Internship\Datasets\UnLabel_Crack\labeled"  # 请替换成你的图像文件夹路径
target_folder = r"D:\Learning\Master\Internship\Datasets\yolo_crack_datasets\images"  # 目标文件夹路径

# 获取所有标注文件
label_files = os.listdir(label_folder)

# 遍历标注文件夹中的所有文件
for label_file in label_files:
    # 如果是.txt文件（标注文件），处理它
    if label_file.endswith(".txt"):
        # 获取第一个'-'及之前的部分并删除
        base_name = label_file.replace('.txt', '')

        # 查找图像文件（假设图像文件扩展名为 .jpg 或 .png）
        image_file_png = base_name + ".png"
        image_file_jpg = base_name + ".jpg"

        # 检查图像文件是否存在
        image_path_png = os.path.join(image_folder, image_file_png)
        image_path_jpg = os.path.join(image_folder, image_file_jpg)

        if os.path.exists(image_path_png):
            image_to_copy = image_path_png
        elif os.path.exists(image_path_jpg):
            image_to_copy = image_path_jpg
        else:
            print(f"没有找到匹配的图片：{base_name}")
            continue

        # 复制图像文件到目标文件夹
        try:
            shutil.copy(image_to_copy, target_folder)
            print(f"已复制图片: {image_to_copy} -> {target_folder}")
        except Exception as e:
            print(f"复制图片时发生错误: {e}")

print("图像文件复制完成！")
