# -*- coding: utf-8 -*-
##题目，Random
from random import randint
from math import floor, sqrt

def genPassword(flag):
    password = ''
    newList = [ord(i) for i in flag ]
    randNum = randint(65, max(newList)) * 255
    for i in range(len(flag)):
        password += str(int(floor(float(randNum + newList[i]) / 2 + sqrt(randNum * newList[i])) % 255)) + ' '
    return password

def deOrder(num, randNum):
    char = ''
    for order in xrange(33, 127):
        if int(floor(float(randNum + order) / 2 + sqrt(randNum * order)) % 255) == num:
            char = chr(order)
    return char

def main():
    password = '208 140 149 236 189 77 193 104 202 184 97 236 148 202 244 199 77 122 113 '
    pswList = [int(num) for num in password[:-1].split(' ')]
    for randNum in xrange(65 * 255, 127 * 255, 255):
        flag = ''
        for num in pswList:
            flag += deOrder(num, randNum)
            
        if len(flag) == len(pswList):
            print 'flag{%s}' % flag

if __name__ == '__main__':
    main()
