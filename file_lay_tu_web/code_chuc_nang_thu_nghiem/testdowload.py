import requests

# URL của file pdf.js từ CDN
url = "https://dhtn.bcy.gov.vn/assets/pdfjs/build/pdf.js"

# Gửi yêu cầu GET để tải file
response = requests.get(url)

# Kiểm tra nếu yêu cầu thành công (status code 200)
if response.status_code == 200:
    # Lưu file vào đường dẫn mong muốn (ví dụ: cùng thư mục với script)
    with open("pdf.js", "wb") as file:
        file.write(response.content)
    print("Tệp pdf.js đã được tải thành công!")
else:
    print(f"Không thể tải tệp. Mã lỗi: {response.status_code}")