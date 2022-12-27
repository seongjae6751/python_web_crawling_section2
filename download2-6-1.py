from bs4 import BeautifulSoup
import re # regular express

html = """
<html><body>
  <ul>
    <li><a id='naver' href="https://www.naver.com">naver</a></li>
    <li><a href="https://www.daum.net">daum</a></li>
    <li><a href="https://www.daum.com">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  <ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
print(soup.find(id='naver').string)
li = soup.find_all(href=re.compile(r"da"))

for e in li:
    print(e.attrs['href'])

# 정규표현식
# http://pythonstudy.xyz/python/article/401-%EC%A0%95%EA%B7%9C-%ED%91%9C%ED%98%84%EC%8B%9D-Regex






