import requests

url = 'https://notify-api.line.me/api/notify'
token = 'Z3nFlOBYdaPDdmLD3FIch5dH35MJywumKXYtjOTLUr5'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': f'Bearer {token}'
}
message =  'test line notify'

message = f"{Local} \n" \
          f"อุณหภูมิ : {temperature} \n" \
          f"สภาพอากาศ : {climate} \n" \


res = requests.post(url=url, headers=headers, data={'message': message})
print(res)