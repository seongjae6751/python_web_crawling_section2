import urllib.request as dw

imgUrl = "https://ssl.pstatic.net/melona/libs/1395/1395430/f03ed14ba2948390b3b4_20220617104525100.jpg"
videoUrl = "https://siape.veta.naver.com/fxclick?eu=EU10041892&calp=-&oj=ZagUyei1lShgXygctONwa9Tl6XBSkiYOJcCoou2SB3mHZ%2FZiSQknFVf1mGj7hJEaAwLM%2B3j6Kpzam2%2FqwK4p9l%2Bg4HPmKQd1wlhFiN83MiptonaOyZyAMXQDCWXx89CCryci2f9DnCAQPHblRNA%2ByMWPj0ecpiqaHUsHbqq%2BK%2BvW8QhOHuq6a3rwEMWmlWBtZJog8DEjB9G3JRglyzW34UA7g35TJtQoH59HDyNQbrbeN2QPWKGpLGvkaJLqEOsvmIZZNRX97ws&ac=8579571&src=5885902&br=3892997&evtcd=P901&x_ti=1316&tb=&oid=&sid1=&sid2=&rk=14d04fb51d68954b39eddc24aad57305&eltts=939RwRdsr%2Fedw3UxE3qbeg%3D%3D&lu=&brs=Y&"

savePath1 = "c://projectimg1.jpg"
savePath2 = "c://projectvideo1.mp4"

dw.urlretrieve(imgUrl,savePath1)
dw.urlretrieve(videoUrl,savePath2)

print("다운로드 완료!")
