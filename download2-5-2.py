from bs4 import BeautifulSoup

html = """
<html>
<body>
<h1>파이썬 BeautifulSoup 공부</h1>
<p>태그 선택자</p> #/n이 사실상 다 되어있음
<p>CSS 선택자</P>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
# print('soup', type(soup))
# print('prettify', soup.prettify()) # 들여쓰기 해줌

h1 = soup.html.body.h1
print('h1', h1)
p1 = soup.html.body.p
print('p1', p1)
p2 = p1.next_sibling.next_sibling
print('p2', p2)
p3 = p1.previous_sibling.previous_sibling
print('p3', p3)

print("h1 >> ", h1.string)
print("p1 >> ", p1.string)
print("p2 >> ", p2.string)




