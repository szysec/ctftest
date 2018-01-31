# -*- coding: utf-8 -*-
##MD5之守株待兔，你需要找到和系统锁匹配的钥匙
##题目链接，http://www.shiyanbar.com/ctf/2040
import time
import hashlib
import requests

url = 'http://ctf5.shiyanbar.com/misc/keys/keys.php'
key = str(int(time.time())-1)
print requests.get(url + '?key=' + key).content
