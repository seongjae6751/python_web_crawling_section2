from bs4 import BeautifulSoup
import urllib.request as req


url= "https://www.inflearn.com/"
res = req.urlopen(url).read().decode(req.urlopen(url).headers.get_content_charset())
soup = BeautifulSoup(res,"html.parser")

recommand = soup.select("div#swiper-wrapper-65db584f59cb63f8 > div#course_title")

print(recommand)
