# -*- coding:utf-8 -*-
##deeeeeeaaaaaadbeeeeeeeeeef-200
##题目链接，http://shiyanbar.com/ctf/1983
def fileReadBinary(path):
    f = open(path, 'rb')
    c = f.read()
    f.close()
    return c

def fileWriteBinary(path, c):
    f = open(path, 'wb')
    f.write(c)
    f.close()
    
def pos(y, x):
    def hexToInt(x):
        return int('0x' + x, 16)   
    return hexToInt(x) + hexToInt(y)

def getHexListFromBinaryFile(path):
    return [hex(ord(i))[2:] for i in fileReadBinary(path)]

def generateBinaryFileFromHexList(path, hexFileList):
    newFile = ''.join([chr(int('0x' + item, 16)) for item in hexFileList])
    fileWriteBinary(path, newFile)
    
def main():
    ##还原图片分辨率
    hexFileList = getHexListFromBinaryFile('0707.png')
    hexFileList[pos('00000010', '06')] = '09'
    hexFileList[pos('00000010', '07')] = '90'
    generateBinaryFileFromHexList('new.png', hexFileList)
        
if __name__ == '__main__':
    main()
