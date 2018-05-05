# -*- coding: utf-8 -*-
##题目，Bubble
from bubblepy import BubbleBabble

def decodeBubble(code):
    bb = BubbleBabble()
    return bb.decode(code)

def main():
    code = 'xinik-samak-luvag-hutaf-fysil-notok-mepek-vanyh-zipef-hilok-detok-damif-cusol-fezyx'
    print decodeBubble(code)

if __name__ == '__main__':
    main()
