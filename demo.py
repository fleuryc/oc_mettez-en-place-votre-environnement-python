import requests


r = requests.get("https://www.clementfleury.me")
print(r.status_code)
