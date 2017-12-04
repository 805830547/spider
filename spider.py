#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests #导入requests库
from bs4 import BeautifulSoup  #导入BeautifulSoup 模块
from selenium import webdriver  #导入Selenium的webdriver
from selenium.webdriver.common.keys import Keys  #导入Keys


#r = requests.get('https://www.baidu.com/') #像目标url地址发送get请求，返回一个response对象.find('tbody')
#print(r.text) #r.text是http response的网页HTML

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}  #给请求指定一个请求头来模拟chrome浏览器
web_url = 'http://music.163.com/#/playlist?id=975380031'
r = requests.get(web_url, headers=headers) #像目标url地址发送get请求，返回一个response对象
all_a = BeautifulSoup(r.text, 'lxml').find_all('a', {'hidefocus':'true'})  #获取网页中的class为cV68d的所有a标签
for a in all_a:
  print(a.href) #循环获取a标签中的style