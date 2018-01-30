# -*- coding: utf-8 -*-
##困在栅栏里的凯撒，解凯撒加密部分，还是用工具吧，比较快...
##题目链接，http://www.shiyanbar.com/ctf/1867
def charToOrderList(string):
    li = []
    for i in string:
        if ord(i) in xrange(65, 91):
           i = ord(i)
        li.append(i)
    return li

def orderListToString(orderList):
    string = ''
    for i in orderList:
        if i in xrange(65, 91):
            string += chr(i)
        else:
            string += i
    return string

def getCaesarList(string):
    caesarList = []
    li = charToOrderList(string.upper())
    for i in xrange(65, 91):
        ls = []
        for j in li:
            if j in xrange(65, 91):
                j = j + 1
                if j >= 91:
                    j -= 26
                ls.append(j)
            else:
                ls.append(j)
        li = ls
        caesarList.append(orderListToString(li).lower())
    return caesarList

string = 'neq{etlydsf}'
for i in getCaesarList(string):
    print i
