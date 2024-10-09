import zipfile
import os

# Đường dẫn tới tệp ZIP đã tải về
zip_file_path = 'ten_tap_tin.zip'  # Thay bằng tên tệp của bạn
extract_folder = 'output_folder'  # Thư mục để giải nén

# Tạo thư mục nếu chưa tồn tại
os.makedirs(extract_folder, exist_ok=True)

# Giải nén tệp ZIP
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

print(f'Tệp đã được giải nén thành công vào thư mục: {extract_folder}')
