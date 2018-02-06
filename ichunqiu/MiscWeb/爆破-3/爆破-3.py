# -*- coding: utf-8 -*-
##题目，爆破-3
import requests
import re

def fileReadLines(path):
    f = open(path, 'r')
    content = f.readlines()
    f.close()
    return content

def findValue(head):
    for string in fileReadLines('dic.txt'):
        if string[:2] == head:
            return string[:-1]

def getContent(session, value):
    content = session.get(url + '?value=' + value).content
    return content

def main():
    url = 'http://1cb5ea0e77c4484888c0c40329b1e90f45527655e100499c.game.ichunqiu.com/'
##    url = 'http://*.game.ichunqiu.com/'
    session = requests.Session()
    head = 'ea'
    for i in xrange(12):
        value = findValue(head)
        content = getContent(session, value)
        head = content[:2]
        
    print re.search('flag{.*}', content).group(0)

if __name__ == '__main__':
    main()
