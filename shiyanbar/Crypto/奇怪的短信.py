# -*- coding: utf-8 -*-
##奇怪的短信
##题目链接，http://www.shiyanbar.com/ctf/1920
##解手机键盘九宫格

def seperateStringToListInPairs(msg):
    li = []
    for i in xrange(len(msg)):
        if not i & 1:
            li.append(msg[i] + msg[i+1])
    return li

def generateStringFromList(li):
    List = [0,1,['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
    return ''.join([List[int(i[0])][int(i[1])-1] for i in li])

def main():
    msg = '335321414374744361715332'
    li = seperateStringToListInPairs(msg)
    flag = generateStringFromList(li)
    print 'CTF{%s}' % flag

if __name__ == '__main__':
    main()
