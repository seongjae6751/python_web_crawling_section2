from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import os

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("사자")
url = base + quote
print(url)

res = req.urlopen(url)
savePath = "C:\\imagedown\\" # C\imagedown\  = C/imagedown/

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != e.errno.EEXIST:
        print("폴더 만들기 실패!")
        raise 

soup = BeautifulSoup(res, "html.parser")

img_list = soup.select("div.thumb > a > img")
print("test", img_list)


for i, div in enumerate(img_list,1):
  print("div =", div['data-source'])
  fullfilename = os.path.join(savePath, savePath+str(i)+'.jpg')
  print(fullfilename)
  req.urlretrieve(div['data-source'],fullfilename)
  print(i)


