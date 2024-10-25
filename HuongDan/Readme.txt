	Lấy file và nội dung từ web của thầy (https://backend8181.bcy.gov.vn) -> phần văn bản đến -> nhận để biết

- B1: Đăng nhập vào trang web thông qua API
https://backend8181.bcy.gov.vn/api/users/login
-> Lấy ra access token
+ vd: 
https://backend8181.bcy.gov.vn/api/users/login?userName=ldthuan@bcy.gov.vn&password=123456 

- B2: Truy cập vào API 
https://backend8181.bcy.gov.vn/api/document/findDocByTypeHandle/2/1
và kèm theo access token lấy được ở B1
-> Lấy được dữ liệu (ngày tháng (đã được mã hoá -> cần giải mã), người gửi, tên văn bản,...) ở trang "Văn bản đến/ Nhận để biết"

+ Giải mã ngày tháng: tham khảo file TimeStamp.py

- B3: Dùng API https://backend8181.bcy.gov.vn/api/attachment/download/{name} 
+ names = [attachment['name'] for obj in data['data']['objList'] for attachment in obj['doc']['attachments']]
-> tải được các file từ trang web của thầy về máy tính, tuy nhiên còn chứa định dạng chưa chuẩn -> định dạng lại file

- B4: Định dạng lại file
# Xóa phần suffix sau dấu gạch dưới cuối cùng
  clean_name = name.split('__')[0]  # Chỉ giữ phần trước dấu gạch dưới (code python)

+ Tham khảo file download_file.py
