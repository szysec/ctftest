import requests
a = open("a","rb").read()
b = open("b","rb").read()

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
##'Cookie': '',                     ##需填写
'Host': '39.107.33.96:10000',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

data = {'param1': a, 'param2': b}
url = 'http://39.107.33.96:10000'

c = requests.post(url, headers = headers, data = data)
print c.content
