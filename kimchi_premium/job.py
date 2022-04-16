import requests
from bs4 import BeautifulSoup
import ccxt

#get dollar value
url = 'https://coinmarketcap.com/ko/currencies/tether'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
select = soup.select('#__next > div.bywovg-1.fUzJes > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div.sc-16r8icm-0.eMxKgr.container > div.n78udj-0.jskEGI > div > div.sc-16r8icm-0.kjciSH.priceSection > div.sc-16r8icm-0.kjciSH.priceTitle > div > span')
Tether_krw = float(str(select[0]).split('₩')[1].split('<')[0].replace(',',''))

#get bitcoin price
binance = ccxt.binance()
upbit = ccxt.upbit()
binance_today_USDT_BTC = binance.fetchTicker('BTC/USDT').get('last')
upbit_today_KRW_BTC = upbit.fetchTicker('BTC/KRW').get('last')
upbit_today_USDT_BTC = upbit_today_KRW_BTC/Tether_krw

#get kimchi premium
kimchi_premium_BTC = str(round((round(upbit_today_USDT_BTC/binance_today_USDT_BTC,4) - 1 )*100, 4)) + '%'
print(kimchi_premium_BTC)