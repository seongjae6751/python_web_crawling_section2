import requests
from bs4 import BeautifulSoup

url= "https://finance.daum.net/api/trend/market_capitalization?page=1&perPage=30&fieldName=marketCap&order=desc&market=KOSPI&pagination=true"
headers ={
    'Referfer' : 'https://finance.daum.net/domestic/market_cap',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

res = requests.get(url, headers=headers)
jsonObj = res.json()
print(jsonObj)

# 비동기
# https://souljit2.tistory.com/7
