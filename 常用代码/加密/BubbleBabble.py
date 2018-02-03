# -*- coding: utf-8 -*-
##Bubble Babble Encoding
from bubblepy import BubbleBabble

def decodeBubble(code):
    bb = BubbleBabble()
    return bb.decode(code)

def encodeBubble(string):
    bb = BubbleBabble()
    return bb.encode(string)

def test():
    string = 'flag{test}'
    code = encodeBubble(string)
    print decodeBubble(code)
    
if __name__ == '__main__':
    test()
