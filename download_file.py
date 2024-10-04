import requests
url ='https://backend8181.bcy.gov.vn/api/users/login?userName=ldthuan@bcy.gov.vn&password=123456'
response = requests.post(url, verify=False)

access_token=''
if response.status_code == 200:
    # Lấy access token từ dữ liệu phản hồi
    json_response = response.json()
    access_token = json_response['data']['tokenInfo']['accessToken']
   
else:
    print(f'Đăng nhập thất bại: {response.status_code}, {response.text}')


print(access_token)
