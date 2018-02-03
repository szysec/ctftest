# -*- coding: utf-8 -*-
##http://www.shiyanbar.com/ctf/741
##题目链接，黑客叔叔（雨袭团）内部交流题（第一季1.0.1）
import base64

##解码base64字符串时抛出异常，解决函数
def decode_base64(data):
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'='* (4 - missing_padding)
    return base64.decodestring(data)

def main():
    ##string = base64.b64decode('dW1mcGJsamhhd3Jmcm14aHoxOXptZjltZWducm13NDV4M2RvbmhxfDAxfDAzfDA3fCt8KzF8KzN8Kzd8MisxfDIrMnwyKzZ8Mis3fDIrOXwzKzB8MyszfDMrN3wzKzh8Mys5fD98')
    string = 'umfpbljhawrfrmxhz19zmf9megnrmw45x3donhq'
    for i in [1, 3, 7, 10, 11, 13, 17, 21, 22, 26, 27, 29, 30, 33, 37, 38, 39]:
        s = string[i-1].upper()
        string = string[0:i-1] + s + string[i:]
    print decode_base64(string)

if __name__ == '__main__':
    main()
