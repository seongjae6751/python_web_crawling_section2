from bs4 import BeautifulSoup
import urllib.request as req

url= "https://finance.naver.com/sise/"
# �ѱ��� ������ ��� ���ڵ� get_content_charset() -> ����Ʈ�� ���ڵ� ����� ������
# r.headers -> ���� ����� {K:V} ������ ��ųʸ� �ڷ��ȯ
res = req.urlopen(url).read().decode(req.urlopen(url).headers.get_content_charset())
soup = BeautifulSoup(res,"html.parser")

top4 = soup.select("#siselist_tab_0 > tr")

i = 1
for e in top4:
    if e.find("a") is not None:
        print(i,e.select_one(".tltle").string)
        i += 1








