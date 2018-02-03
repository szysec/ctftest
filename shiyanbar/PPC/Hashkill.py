# -*- coding: utf-8 -*-
##Hashkill
##题目链接，http://www.shiyanbar.com/ctf/1807
import hashlib

md5OfFlag = '6ac66ed89ef9654cf25eb88c21f4ecd0'
districtOfNewYork = [d.lower() for d in ['TheBronx', 'Brooklyn', 'Manhattan', 'Queens', 'StatenIsland']]##注意区名用小写
for i in xrange(0, 1001):
    for d in districtOfNewYork:
        for j in xrange(10000, 15001):
            flag = 'ctf{' + str(i) + '_' + d + '_' + str(j) + '}'
            if(hashlib.md5(flag).hexdigest() == md5OfFlag):
                print flag
                input()
