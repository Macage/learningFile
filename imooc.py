#!/usr/bin/env python
#coding:utf-8

import urllib2
from bs4 import BeautifulSoup
import json
andr = {}#新建一个大字典
#查看关于android课程的所有page页面
for i in range(1,6):
    url = 'http://www.imooc.com/course/list?c=android&page=%d' % i#拼接每一个页面的url
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    moco_info = soup.find('div',{'class':'moco-course-list'})
    moco_list = moco_info.find_all('div',{'class':'moco-course-wrap'})
    page = 'page_' + str(i)#获取6个不同的page，如page_1表示第一个页面
    page = []#建立第一个page空列表，相当于容器，把这个页面的所有的课程放进去
    for moco in moco_list:
        if len(moco.find_all('a')) > 1:continue
        cla_url = moco.find('a').get('href')#获取该page的每一个课程url
        cla_id = cla_url.split('/')[-1]
        url = 'http://www.imooc.com%s' % cla_url
        html = urllib2.urlopen(url).read()
        cla_info = BeautifulSoup(html,'lxml')
        course_name = cla_info.find('div',{'class':'hd'}).text.strip()
        cl_info = cla_info.find('div',{'class':'statics'})
        cla = cl_info.find_all('div',{'class':'static-item'})
        clas_info = {}#每一个课程对应一个id号与课程信息放入该字典中
        class_info = {}#所有信息放入这个字典中
        class_info[u'课程名称'] = course_name
        for cl in cla:
            meta_key = cl.find('span',{'class':'meta'}).text
            meta_value = cl.find('span',{'class':'meta-value'}).text
            class_info[meta_key] = meta_value
        clas_info[cla_id] = class_info
        page.append(clas_info)#将该课程内容填充到page列表中
    andr[str(i)] = page
#print andr
f = open('imooc.txt','w')
json.dump(andr,f)#将大字典写入txt文档
f.close()
