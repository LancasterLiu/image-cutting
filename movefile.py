import os  
import shutil  
  
# 定义源文件夹和目标文件夹  
source_folder = '../self'  # 父文件夹  
  
# 遍历源文件夹中的每个子文件夹  
for sub_folder in os.listdir(source_folder):  
    sub_folder_path = os.path.join(source_folder, sub_folder)  
      
    # 确保子文件夹是真实的文件夹而不是文件  
    if os.path.isdir(sub_folder_path):  
        # 遍历子文件夹中的每个文件  
        for file_name in os.listdir(sub_folder_path):  
            file_path = os.path.join(sub_folder_path, file_name)  
              
            # 检查文件名前缀，并确定目标文件夹  
            prefix = file_name.split('_')[0]  
            target_folder_path = os.path.join(source_folder, prefix)  
                  
            # 将文件移动到目标文件夹  
            shutil.move(file_path, os.path.join(target_folder_path, file_name))  
            print(f'Moved: {file_path} -> {os.path.join(target_folder_path, file_name)}')