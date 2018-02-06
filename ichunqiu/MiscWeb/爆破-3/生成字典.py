# -*- coding: utf-8 -*-
import hashlib
import random

def fileWrite(path, content):
    f = open(path, 'w')
    f.write(content)
    f.close()

def genString(value, alphabet):
    for i in xrange(1000000):
        string = value
        string += random.choice(alphabet)
        string += random.choice(alphabet)
        string += random.choice(alphabet)
        string += random.choice(alphabet)
        string += random.choice(alphabet)
        string += random.choice(alphabet)
        if hashlib.md5(string).hexdigest()[5:9] == '0000':
            return string
    return 'None'

def main():
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    text = ''
    for i in alphabet:
        for j in alphabet:
            value = i + j
            string = genString(value, alphabet)
            text += string + '\n'
    fileWrite('dic.txt', text)

if __name__ == '__main__':
    main()
