from bs4 import BeautifulSoup

html = """
<html><body>
  <ul>
    <li><a href="https://www.naver.com">naver</a></li>
    <li><a href="https://www.daum.net">daum</a></li>
    <li><a href="https://www.daumdc.com">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  <ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a")
# print('links',type(links))
a = soup.find_all("a", string='daum')
print('a',a)
b = soup.find_all("a", limit=3)
print('b',b)
c = soup.find_all(string = ["naver", "google"])
print('c', type(c))

for a in links:
    # print('a',type(a), a)
    href = a.attrs['href'] # attrs 속성 값을 모두 가져옴 # 키 값으로 접근
    txt = a.string # string 문자? 가져옴 # 직접 접근
    # print('txt >> ', txt, 'href >> ', href)










