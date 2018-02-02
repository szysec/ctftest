# -*- coding: utf-8 -*-
def decodePawnshop(char):
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
    if char in dic:        
        return dic[char]
    else:
        return char

def decrypt(text):
    return ''.join([str(decodePawnshop(char)) for char in text])

##解码数字为ascii字符
def asciiOrderToChar(text):
    return ''.join([chr(int(char)) for char in text.split(' ')])    

def test():
    text = u'大 井 中'
    print decrypt(text)
    
if __name__ == '__main__':
    test()
