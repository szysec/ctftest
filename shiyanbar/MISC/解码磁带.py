# -*- coding: utf-8 -*-
##解码磁带
##题目链接，http://www.shiyanbar.com/ctf/1891
def getCharFromCode(code):
    f = lambda char:'1' if char == 'o' else '0'
    asciiCode = ''.join([f(char) for char in code])
    return chr(int(asciiCode, 2))

def getStringFromText(text):
    return ''.join([transform(string) for string in text.split(' ')])

def main():
    text = '''
        o____o_ 
        oo__o_o 
        oo_o__o 
        oo_o_o_ 
        oo_o__o 
        oo_ooo_ 
        oo__ooo 
        _o_ooo_
        '''
    print getStringFromText(text)

if __name__ == '__main__':
    main()
