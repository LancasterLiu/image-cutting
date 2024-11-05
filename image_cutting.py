import os  
from PIL import Image  
  
def parse_annotation_with_id(annotation_path, image_width, image_height):  
    """  
    解析YOLO格式的标注文件，返回标注框的列表。  
    标注文件的格式是每行一个标注框，格式为 "label x_center y_center width height"。  
    这里假设坐标是归一化的，如果需要像素坐标，则需要在函数内部进行转换。  
    """  
    with open(annotation_path, 'r') as file:  
        lines = file.readlines()  
        boxes = []  
        for line in lines:  
            label,id, x_center, y_center, width, height = map(float, line.strip().split())  
            label=int(label)
            id=str(int(id)+1510)
            # 如果坐标是归一化的，则转换为像素坐标  
            x_center_px = int(x_center * image_width)  
            y_center_px = int(y_center * image_height)  
            width_px = int(width * image_width)  
            height_px = int(height * image_height)  
              
            # 计算边界框的左上角坐标  
            x_min_px = x_center_px - width_px // 2  
            y_min_px = y_center_px - height_px // 2  
              
            # 确保边界框在图像范围内（如果需要）  
            x_min_px = max(0, x_min_px)  
            y_min_px = max(0, y_min_px)  
            x_max_px = min(image_width, x_center_px + width_px // 2)  
            y_max_px = min(image_height, y_center_px + height_px // 2)  
              
            # 更新宽度和高度以适应可能的调整  
            width_px = x_max_px - x_min_px  
            height_px = y_max_px - y_min_px  
              
            # 将调整后的边界框添加到列表中  
            boxes.append((label,id, x_min_px, y_min_px, width_px, height_px))  
    return boxes  
    
def cut_and_save_images_with_id(image_path, annotation_path, output_folder):  
    """  
    根据YOLO格式的标注文件切割图像并保存到输出文件夹。  
    """  
    image = Image.open(image_path)  
    image_width, image_height = image.size  
      
    boxes = parse_annotation_with_id(annotation_path, image_width, image_height)  

    # if len(boxes)!=1:
    #     return
    for idx, (label,id, x_min, y_min, width, height) in enumerate(boxes):  
        if not os.path.exists(output_folder+'/'+id):
            os.makedirs(output_folder+'/'+id)
        
        # 切割图像  
        cut_image = image.crop((x_min, y_min, x_min + width, y_min + height))  
        if image is not None and image.width > 0 and image.height > 0:
            # 构造输出文件名并保存切割后的图像
            base_name = os.path.splitext(os.path.basename(image_path))[0]  
            output_filename = f"{id}_{base_name}.jpg"  
            output_path = os.path.join(output_folder+'/'+id, output_filename)  
            cut_image.save(output_path)  
        print(f"Saved {output_path}")  

def process_images_in_folder(input_folder, output_folder, head=False, with_id=False):  
    """  
    处理输入文件夹中的所有图像和YOLO格式的标注文件。  
    """  
    if not os.path.exists(output_folder):  
        os.makedirs(output_folder)  
      
    for r,dirs,f in os.walk(input_folder):
        for dir in dirs:
            img_dir=os.path.join(input_folder, dir)
            for filename in os.listdir(img_dir):  
                if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):  
                    image_path = os.path.join(img_dir, filename)  
                    annotation_filename = os.path.splitext(filename)[0] + '.txt'  
                    annotation_dir= os.path.join('labels path', dir)
                    annotation_path = os.path.join(annotation_dir, annotation_filename)  
                    
                    if os.path.exists(annotation_path):  
                        # 切割并保存图像  
                        cut_and_save_images_with_id(image_path, annotation_path, output_folder)
                    else:  
                        print(f"Annotation file for {filename} not found.")  

input_folder = 'image path'  # 图像文件夹路径  
output_folder = 'output path'  # 输出文件夹

# 处理图像
process_images_in_folder(input_folder, output_folder)
