import os
import shutil

# 다운로드 폴더 경로
download_folder = 'C:\\Users\\student\\Downloads'

# 이동할 폴더 경로들
destination_folders = {
    'images': os.path.join(download_folder, 'images'),
    'data': os.path.join(download_folder, 'data'),
    'docs': os.path.join(download_folder, 'docs'),
    'archive': os.path.join(download_folder, 'archive')
}

# 폴더 생성
for folder_path in destination_folders.values():
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# 이동할 파일 유형들
file_types = {
    'images': ['.jpg', '.jpeg'],
    'data': ['.csv', '.xlsx'],
    'docs': ['.txt', '.doc', '.pdf'],
    'archive': ['.zip']
}

# 파일 이동
for file in os.listdir(download_folder):
    file_path = os.path.join(download_folder, file)
    if os.path.isfile(file_path):
        for folder_name, extensions in file_types.items():
            for ext in extensions:
                if file.lower().endswith(ext):
                    shutil.move(file_path, os.path.join(destination_folders[folder_name], file))
                    break


