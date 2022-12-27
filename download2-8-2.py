# 나중에 다시 할것
# ajax 형식으로 현재 다 변함






from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import os

base = ""
quote = rep.quote_plus("")
url = base + quote


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

img_list = soup.select("")
print("test", img_list)


for i, div in enumerate(img_list,1):
  print("div =", div['data-source'])
  fullfilename = os.path.join(savePath, savePath+str(i)+'.jpg')
  print(fullfilename)
  req.urlretrieve(div['data-source'],fullfilename)
  print(i)


