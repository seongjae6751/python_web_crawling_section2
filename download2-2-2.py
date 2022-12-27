import urllib.request as dw

imgUrl = "https://search.pstatic.net/sunny/?src=http%3A%2F%2Fdown.humoruniv.com%2Fhwiparambbs%2Fdata%2Feditor%2Fpdswait%2Fe_s7655cd006_ee859578f94813ae04bfa3fd12b101f252154af8.jpg&type=sc960_832"
htmlURL = "http://google.com"

savePath1 = "c:/test1.jpg"
savePath2 = "c://index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()
# open은 파일 생성
saveFile1 = open(savePath1, 'wb') # w : write, r : read, a : add
# write는 파일에 문자열 넣어줌
saveFile1.write(f)
saveFile1.close()
# 참고 자료 -> https://blockdmask.tistory.com/454

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료!")

# urlretrieve 와 urlopen의 차이
# urlretrieve:
# 저장 -> open("r") -> 변수에 할당 -> 파싱 -> 저장
# urlopen:
# 변수할당 -> 파싱 -> 저장(db..)
