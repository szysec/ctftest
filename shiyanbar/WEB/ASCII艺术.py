# -*- coding: utf-8 -*-
##ASCII艺术
##题目链接，http://www.shiyanbar.com/ctf/1843 
import requests
import re

def transform(text):
    text = text.replace('&nbsp;xxx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x<br />x&nbsp;&nbsp;&nbsp;x<br />x&nbsp;&nbsp;&nbsp;x<br />&nbsp;xxx&nbsp;<br />','0')
    text = text.replace('&nbsp;xx<br>&nbsp;&nbsp;x&nbsp;x&nbsp;&nbsp;<br>&nbsp;&nbsp;x&nbsp;&nbsp;<br>&nbsp;&nbsp;x&nbsp;&nbsp;<br>xxxxx<br>','1')
    text = text.replace('&nbsp;xxx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x&nbsp;<br />&nbsp;&nbsp;xx&nbsp;<br />&nbsp;x&nbsp;&nbsp;&nbsp;<br />xxxxx<br />','2')
##    text = text.replace('','3')
    text = text.replace('&nbsp;x&nbsp;&nbsp;&nbsp;x<br />x&nbsp;&nbsp;&nbsp;&nbsp;x<br />&nbsp;xxxxx<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br />&nbsp;&nbsp;&nbsp;&nbsp;x<br />','4')
    text = text.replace('xxxxx<br />x&nbsp;&nbsp;&nbsp;&nbsp;<br />&nbsp;xxxx<br />&nbsp;&nbsp;&nbsp;&nbsp;x<br />xxxxx<br />','5')
##    text = text.replace('','6')
##    text = text.replace('','7')
    text = text.replace('&nbsp;xxx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x<br />&nbsp;&nbsp;xx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x<br />&nbsp;xxx&nbsp;<br />','8')
    text = text.replace('<br/>',' ')
    text = text.replace('  ',' ')
    text = text.replace('  ',' ')
    text = text.replace(' ','')
    return text

def main():
    url = 'http://ctf5.shiyanbar.com/ppc/acsii.php'
    session = requests.Session()
    content = session.get(url).content
    div = re.search('<div name=\'sha1\' style="color:red">(.*?)</div>', content).group(1)
    payload = {'inputNumber': transform(div), 'submit': '%E6%8F%90%E4%BA%A4'}
    print session.post(url, data = payload).content

if __name__ == '__main__':
    main()
