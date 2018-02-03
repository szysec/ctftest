# -*- coding:utf-8 -*-
##找素数
##题目链接，http://www.shiyanbar.com/ctf/1922
import math

def isPrime(n):
    if n <= 1: 
        return False 
    for i in range(2, int(math.sqrt(n)) + 1): 
        if n % i == 0: 
            return False 
    return True

a = 367
c = 1
while c <= 151:
    if isPrime(a):
        print c, a
        c += 1
    a = a + 186
