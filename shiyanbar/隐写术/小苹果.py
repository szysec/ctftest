# -*- coding: utf-8 -*-
##小苹果，当铺密码部分
##题目链接，http://www.shiyanbar.com/ctf/1928

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

string = '\u7f8a\u7531\u5927\u4e95\u592b\u5927\u4eba\u738b\u4e2d\u5de5'
print string.decode('unicode-escape')
print ''.join([str(dic[char]) for char in string.decode('unicode-escape')])
