from bs4 import BeautifulSoup
import urllib.request as req

url= "https://finance.naver.com/sise/"
# 한글이 깨지는 경우 디코딩 get_content_charset() -> 사이트의 인코딩 방식을 가져옴
# r.headers -> 응답 헤더의 {K:V} 형식의 딕셔너리 자료반환
res = req.urlopen(url).read().decode(req.urlopen(url).headers.get_content_charset())
soup = BeautifulSoup(res,"html.parser")

top4 = soup.select("#siselist_tab_0 > tr")

i = 1
for e in top4:
    if e.find("a") is not None:
        print(i,e.select_one(".tltle").string)
        i += 1








