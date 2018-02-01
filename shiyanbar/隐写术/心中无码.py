# -*- coding: utf-8 -*-
##心中无码
##题目链接，http://www.shiyanbar.com/ctf/1947
from PIL import Image
img = Image.open('Lena.png')
width, height = img.size

text = ''
for w in xrange(width):
    for h in xrange(height):
        pixel = img.getpixel((w, h))
        if pixel != (255, 255, 0):
            if pixel[2] & 1:
                text += '\x00\x00\x00'
            else:
                text += '\xff\xff\xff'
mode = 'RGB'
img2 = Image.frombuffer(mode, (300, 300), text, 'raw', mode, 0, 1)
img2.save('new.png')
