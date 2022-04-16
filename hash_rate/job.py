import requests

url = 'https://blockchain.info/q/hashrate'

html = requests.get(url)
gigahash = int(html.text)
Terahash = round(gigahash/1000,2)/1000000