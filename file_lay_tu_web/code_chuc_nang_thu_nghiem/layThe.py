import requests
from bs4 import BeautifulSoup

# Tạo session để duy trì đăng nhập
session = requests.Session()

# URL trang đăng nhập
login_url = "https://dhtn.bcy.gov.vn/login"

# Thông tin đăng nhập của bạn
login_data = {
    'username': 'ldthuan@bcy.gov.vn',
    'password': '123456'
}

# Đăng nhập vào trang web bằng POST
login_response = session.get(login_url, data=login_data, verify=False)

# Kiểm tra đăng nhập có thành công không
if login_response.status_code == 200:
    print("Đăng nhập thành công!")

    # Truy cập trang cần lấy dữ liệu sau khi đăng nhập
    data_url = "https://dhtn.bcy.gov.vn/document-in/list/draft-detail/38929?tab=CHO_XU_LY"
    data_response = session.get(data_url, verify=False)

    # Kiểm tra trạng thái phản hồi
    if data_response.status_code == 200:
        # Phân tích cú pháp HTML
        soup = BeautifulSoup(data_response.text, 'html.parser')
        
        # Tìm tất cả các thẻ <p>
        p_elements = soup.find_all('p')
        
        # In nội dung của tất cả các thẻ <p>
        for p in p_elements:
            print(p.text)  # Hoặc dùng p.get_text() để lấy nội dung văn bản
    else:
        print(f"Không thể truy cập trang dữ liệu: {data_response.status_code}")
else:
    print(f"Đăng nhập thất bại: {login_response.status_code}")
