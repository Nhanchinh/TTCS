	Lấy file và nội dung từ web của thầy (https://backend8181.bcy.gov.vn) -> phần văn bản đến -> nhận để biết

- B1: Đăng nhập vào trang web thông qua API
https://backend8181.bcy.gov.vn/api/users/login
-> Lấy ra access token
+ vd: 
https://backend8181.bcy.gov.vn/api/users/login?userName=ldthuan@bcy.gov.vn&password=123456 

- B2: Truy cập vào API
https://backend8181.bcy.gov.vn/api/document/findDocByTypeHandle/2/1
