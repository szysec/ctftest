@echo off
::需要安装openssl
::需要msieve153

set openssl="...\openssl.exe"
set msieve="...\msieve153.exe"
set publicPem=".\public.pem"

%openssl% rsa -pubin -text -modulus -in %publicPem%|findstr "Modulus=">mod.txt
for /f %%s in (mod.txt) do (
    set text=%%s
)
set mod=0x%text:~8,64%
%msieve% %mod% -v>temp.txt
type temp.txt|findstr p39>>mod.txt

py -2 getPriv.py
%openssl% rsautl -decrypt -in flag.enc -inkey private.pem
%openssl% rsautl -decrypt -in flag.enc -inkey private.pem>flag.txt

del temp.txt
del msieve.log
del msieve.dat
del private.pem
del mod.txt

echo .
pause
exit