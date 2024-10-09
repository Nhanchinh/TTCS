import requests

# Địa chỉ API đăng nhập
url = 'https://backend8181.bcy.gov.vn/api/users/login?userName=ldthuan@bcy.gov.vn&password=123456'

# Gửi yêu cầu đăng nhập
response = requests.post(url, verify=False)

access_token = ''
if response.status_code == 200:
    # Lấy access token từ dữ liệu phản hồi
    json_response = response.json()
    access_token = json_response['data']['tokenInfo']['accessToken']
else:
    print(f'Đăng nhập thất bại: {response.status_code}, {response.text}')
    exit()  # Thoát nếu đăng nhập thất bại

# Đặt tiêu đề Authorization với access token
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'  # nếu cần
}
print(f'Access Token: {access_token}')

# Địa chỉ API để tìm tài liệu
url1 = 'https://backend8181.bcy.gov.vn/api/document_out/knowable?page=2&sortBy=&direction=DESC&size=10&read=false'
# Gửi yêu cầu lấy tài liệu
response1 = requests.get(url1, headers=headers, verify=False)

if response1.status_code == 200:
    data = response1.json()  # Chuyển đổi phản hồi thành JSON
    # Lấy tên từ các attachments
    names = [attachment['name'] for obj in data['data']['content'] for attachment in obj['attachments']]
    print("Các tệp sẽ được tải xuống:", names)

    # Vòng lặp để tải xuống từng tệp
    for name in names:
        download_url = f'https://backend8181.bcy.gov.vn/api/doc_out_attach/download/{name}'  # Địa chỉ tải xuống
        response_download = requests.get(download_url, headers=headers, verify=False)

        if response_download.status_code == 200:
            # Xóa phần suffix sau dấu gạch dưới cuối cùng
            clean_name = name.split('__')[0]  # Chỉ giữ phần trước dấu gạch dưới
            # Lưu tệp vào hệ thống
            with open(clean_name, 'wb') as f:
                f.write(response_download.content)
            print(f'Tải xuống thành công: {clean_name}')
        else:
            print(f'Error tải xuống {name}: {response_download.status_code}, {response_download.text}')
else:
    print(f'Error: {response1.status_code}, {response1.text}')
