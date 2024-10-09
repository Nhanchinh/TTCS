import datetime

# Các giá trị timestamp (tính bằng mili giây)
create_date_ms = 1719394305509
update_date_ms = 1719449747658

# Chuyển đổi từ mili giây sang giây
create_date_sec = create_date_ms / 1000
update_date_sec = update_date_ms / 1000

# Chuyển đổi sang ngày tháng
create_date = datetime.datetime.fromtimestamp(create_date_sec).strftime('%d/%m/%Y')
update_date = datetime.datetime.fromtimestamp(update_date_sec).strftime('%d/%m/%Y')

print(f'Create Date: {create_date}')
print(f'Update Date: {update_date}')
