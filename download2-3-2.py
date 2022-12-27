import urllib.request as req
from urllib.parse import urlencode #urllib.parse 패키지에서 urlencode 모듈을 가져온다는 뜻

API = "https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/bachelorList.do"
values = {
    'mCode': 'MN233'
}
print('before', values)
params = urlencode(values) # url로 인코딩한 문자열을 반환
print('after',params)

url = API + "?" + params
print("요청 url", url)

reqData = req.urlopen(url).read().decode('utf-8')
print("출력",reqData)

# 참조
# urlparse = https://dev-dain.tistory.com/50
# api = https://dev-dain.tistory.com/50




