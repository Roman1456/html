import requests

url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
r = requests.get(url)

if r.status_code == 200:
    data = r.json()
    print(data)
else:
    print("помилка")
