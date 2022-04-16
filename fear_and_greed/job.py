import requests

url = 'https://api.alternative.me/fng/?limit=10000'

response = requests.get(url)
text = response.json()

print(text)