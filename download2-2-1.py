import urllib.request as dw

imgUrl = "https://search.pstatic.net/sunny/?src=http%3A%2F%2Fdown.humoruniv.com%2Fhwiparambbs%2Fdata%2Feditor%2Fpdswait%2Fe_s7655cd006_ee859578f94813ae04bfa3fd12b101f252154af8.jpg&type=sc960_832"
htmlURL = "http://google.com"

savePath1 = "c:/test1.jpg"
savePath2 = "c://index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(imgUrl, savePath2)

print("다운로드 완료!")
