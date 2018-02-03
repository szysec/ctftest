# -*- coding: utf-8 -*-
##紧急报文
##题目链接，http://shiyanbar.com/ctf/1955

##解ADFGX密码(ADFGX Cipher)
def ADFGXCipher(x, y):
    dic = {'A': 0, 'D': 1, 'F': 2, 'G': 3, 'X': 4}
    l = ['p', 'h', 'q', 'g', 'm', 'e', 'a', 'y', 'n', 'o', 'f', 'd', 'x', 'k', 'r', 'c', 'v', 's', 'z', 'w', 'b', 'u', 't', 'i', 'l']
    return l[dic[x] * 5 + dic[y]]

def decrypt(text):    
    s = ''
    for i in text.split(' '):
        x, y = i[0], i[1]
        s += ADFGXCipher(x, y)
    return s

def main():
    text = 'FA XX DD AG FF XG FD XG DD DG GA XF FA'
    print 'flag_Xd{hSh_ctf:%s}' % decrypt(text)

if __name__ == '__main__':
    main()
