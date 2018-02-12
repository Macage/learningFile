import urllib.request
from bs4 import BeautifulSoup
import json

sql_class = []

url = "http://www.imooc.com/course/list?c=mysql"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'lxml')
moco_info = soup.find('div',{'class':'moco-course-list'})
moco_list = moco_info.find_all('div',{'class':'index-card-container'})
print(len(moco_list))
for moco in moco_list:
    cla_url = moco.find('a').get('href')
    cla_id = cla_url.split('/')[-1]
    print(cla_id)
    url = "http://www.imooc.com%s" % cla_url
    html = urllib.request.urlopen(url).read()
    cla_info = BeautifulSoup(html,'lxml')
    course_name = cla_info.find('div',{'class':'hd'}).text.strip()
    cla = cla_info.find_all('div',{'class':'static-item'})
    clas_info = {}
    clas_info['class_id'] = cla_id
    for cl in cla:
        meta_key = cl.find('span',{'class':'meta'}).text
        meta_value = cl.find('span',{'class':'meta-value'}).text
        clas_info[meta_key] = meta_value
    sql_class.append(clas_info)
f = open('imooc1.txt','w')
json.dump(sql_class,f)
f.close()
