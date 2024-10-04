import requests

url = "https://backend8181.bcy.gov.vn/api/hstl/getHosoByDocIdAndDocType"
params = {
    'docId': 71622,
    'docType': 'VAN_BAN_DEN'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    print(response.json())  # In kết quả nếu thành công
else:
    print(f"Error: {response.status_code}")
