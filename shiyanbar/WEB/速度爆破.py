# -*- coding: utf-8 -*-
##速度爆破
##题目链接，http://www.shiyanbar.com/ctf/1841
import hashlib
import requests
##from bs4 import BeautifulSoup
import re##用正则执行速度比较快

dic = {}
for i in xrange(1, 100001):
    valueOfMd5 = hashlib.md5(str(i)).hexdigest()
    valueOfSha1 = hashlib.sha1(valueOfMd5).hexdigest()
    dic[valueOfSha1] = i
    
url = 'http://ctf5.shiyanbar.com/ppc/sd.php'
session = requests.Session()##注意此处用Session模拟登录
content = session.get(url).content
##sha1 = BeautifulSoup(content, "html.parser").find('div', {'name': 'sha1'}).text
sha1 = re.search('<div name=\'sha1\' style="color:red">(.*?)</div>', content).group(1)
payload = {'inputNumber': dic[sha1], 'submit': '%E6%8F%90%E4%BA%A4'}
print session.post(url, data = payload).content
