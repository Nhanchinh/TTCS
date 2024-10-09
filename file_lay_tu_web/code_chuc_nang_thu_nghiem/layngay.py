import requests
from bs4 import BeautifulSoup

url = 'https://dhtn.bcy.gov.vn/document-in/list/draft-detail/38929?tab=CHO_XU_LY'

# Bước 1: Gửi yêu cầu HTTP đến trang web (bỏ qua xác minh chứng chỉ)
response = requests.get(url, verify=False)

# Bước 2: Phân tích HTML bằng BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Bước 3: Tìm thẻ <p> theo class
class_name = 'form-control-static'
p_tag = soup.find('p', class_=class_name)

# Bước 4: Lấy nội dung
if p_tag:
    print(p_tag.text)
else:
    print("Không tìm thấy thẻ <p> với class đã chỉ định.")
