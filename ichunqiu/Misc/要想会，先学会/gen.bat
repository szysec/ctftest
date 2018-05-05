@echo off
tshark -r p.pcapng icmp>tmp && py -3 main.py && del tmp
pause>nul
exit