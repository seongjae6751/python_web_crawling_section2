import urllib.request as req
from urllib.parse import urlparse

url = "https://www.encar.com"

mem = req.urlopen(url)

# print(type(mem))
# print(type({}))
# print(type([]))
# print(type(()))

# print("geturl",mem.geturl())
# print("status",mem.status) #200, 404, 403, 500
# print("headers", mem.getheaders())
# print("info", mem.info())
# print("code",mem.getcode())
# print("read",mem.read(50).decode("utf-8")) #euc-kr .... # read()는 html 파일을 읽어옴
print(urlparse("http://www.encar.com?test=test"))




