# -*- coding: utf-8 -*-
##小苹果，当铺密码部分
##题目链接，http://www.shiyanbar.com/ctf/1928

def decodePawnshop(char):
    dic = {u'口': 0,
           u'由': 1,
           u'中': 2,
           u'人': 3,
           u'工': 4,
           u'大': 5,
           u'王': 6,
           u'夫': 7,
           u'井': 8,
           u'羊': 9,}
    if char in dic:        
        return dic[char]
    else:
        return char

def decrypt(text):
    return ''.join([str(decodePawnshop(char)) for char in text])

def main():
    string = '\u7f8a\u7531\u5927\u4e95\u592b\u5927\u4eba\u738b\u4e2d\u5de5'
    text = string.decode('unicode-escape')
    print decrypt(text)

if __name__ == '__main__':
    main()
