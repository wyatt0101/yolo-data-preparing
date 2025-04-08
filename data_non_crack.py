import os

# 定义图片和标注文件夹路径
image_folder = r"D:\Learning\Master\Internship\Datasets\Non_Crack\images"
label_folder = r"D:\Learning\Master\Internship\Datasets\Non_Crack\labels"

# 确保 labels 文件夹存在
os.makedirs(label_folder, exist_ok=True)

# 获取所有图片文件名（只取文件名，不含扩展名）
image_files = [f for f in os.listdir(image_folder) if f.endswith((".jpg", ".png"))]

# 为每张图片生成对应的空标注文件
for image_file in image_files:
    label_file = os.path.splitext(image_file)[0] + ".txt"  # 替换扩展名为 .txt
    label_path = os.path.join(label_folder, label_file)

    # 创建空的.txt文件
    open(label_path, "w").close()

print(f"已成功在 {label_folder} 生成 {len(image_files)} 个空标注文件！")
