@echo off
::A记录
::题目链接，http://www.shiyanbar.com/ctf/1853
set capFile=shipin.cap
set pathOfTools=\aircrack-ng-1.2-rc4-win\bin\64bit
set aircrack=%pathOfTools%\aircrack-ng-avx.exe
set airdecap=%pathOfTools%\airdecap-ng.exe
::%aircrack% %capFile%
::%aircrack% -w wordlist.txt %capFile%
%airdecap% %capFile% -e 0719 -p 88888888
pause