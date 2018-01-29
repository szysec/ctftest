##python 3.6
##天下武功唯快不破
##题目链接，http://www.shiyanbar.com/ctf/1854
from urllib import request, parse
import re
import base64

def getKeyFromHeaders(headers):
    flag = re.search('FLAG: (.*?)\n', str(headers)).group(1)##get flag in response headers
    key = re.search(':(.*?)\'$', str(base64.b64decode(flag))).group(1)##decode base64
    return key

def getKey(url, key):
    req = request.Request(url)
    payload = parse.urlencode([('key',key)]).encode('utf-8')
    response = request.urlopen(req, data = payload)
    print(str(response.read()))

url = 'http://ctf5.shiyanbar.com/web/10/10.php' 
response = request.urlopen(url)
print(str(response.read()))
key = getKeyFromHeaders(response.info())
getKey(url, key)
    
