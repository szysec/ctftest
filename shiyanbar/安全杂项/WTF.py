# -*- coding: utf-8 -*-
##WTF?
##题目链接，http://www.shiyanbar.com/ctf/1886
import base64
from PIL import Image, ImageDraw

def fileRead(path):
    f = open(path, 'r')
    content = f.read()
    f.close()
    return content

def fileWrite(path, content):
    f = open(path,'w')
    f.write(content)
    f.close()

def generateQrcodePhotoFromList(ls, path, types):
    width, height = 256, 256
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    for x in xrange(width):
        for y in xrange(height):
            draw.point((x, y), fill = ls[x*256+y])
    image.save(path, types)
    
def main():    
    content = fileRead('code.txt')
    text = base64.b64decode(content)

    ls = []
    for char in text:
        if char == '0':
            ls.append((255, 255, 255))
        else:
            ls.append((0, 0, 0))

    generateQrcodePhotoFromList(ls, 'code.jpg', 'jpeg')
    
if __name__ == '__main__':
    main()
