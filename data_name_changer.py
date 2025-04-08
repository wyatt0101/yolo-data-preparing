import os


# 设置标注文件和图像文件的路径
label_folder = r""  # 请替换成你的标注文件夹label路径
image_folder = r""  # 请替换成你的图像文件夹images路径

# 获取所有标注文件
label_files = os.listdir(label_folder)

for label_file in label_files:
    # 如果是.txt文件（标注文件），处理它
    if label_file.endswith(".txt"):
        # 获取标注文件的前缀部分（即 '-' 前的字符）
        # 获取第一个'-'及之前的部分并删除
        base_name = label_file.split('-', 1)[-1].replace('.txt', '')  # 只分割一次

        # 查找图像文件（假设图像文件扩展名为 .jpg 或 .png）
        # 你可以根据你的情况扩展支持其他图像格式
        image_file_png = base_name + ".png"
        image_file_jpg = base_name + ".jpg"

        # 检查图像文件是否存在
        if os.path.exists(os.path.join(image_folder, image_file_png)):
            new_label_name = base_name + ".txt"
        elif os.path.exists(os.path.join(image_folder, image_file_jpg)):
            new_label_name = base_name + ".txt"
        else:
            print(f"没有找到匹配的图片：{label_file}")
            continue

        # 获取旧的标注文件路径
        old_label_path = os.path.join(label_folder, label_file)
        # 获取新的标注文件路径
        new_label_path = os.path.join(label_folder, new_label_name)

        # 重命名文件
        os.rename(old_label_path, new_label_path)
        print(f"标注文件已重命名: {label_file} -> {new_label_name}")

print("所有标注文件已处理完毕！")



