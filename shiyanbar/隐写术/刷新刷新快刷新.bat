@echo off
::刷新 刷新 快刷新
::链接地址，http://www.shiyanbar.com/ctf/1938
::工具链接，https://github.com/matthewgao/F5-steganography
set location="图片位置"
set pic=%location%\123456.jpg
set out=%location%\output.txt
set psw=123456
java Extract %pic% -p %psw% -e %out%
type %out%
del %out%
pause