# -*- coding:utf-8 -*-
##小猴子爱吃桃子
##题目链接，http://www.shiyanbar.com/ctf/2048
##
##猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个 第二天早上又将剩
##下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下 
##的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
momo = 1
print 'Day 10:', momo
for i in xrange(1,10):
    momo = (momo + 1) * 2
    print 'Day', 10-i, ':', momo
