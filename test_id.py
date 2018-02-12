#coding:utf-8

f = open('id_list.txt', 'r+')
results = [id0.strip() for id0 in f.readlines()]
f.close()
fp = open('url.txt', 'w')
for id0 in results:
    url = 'http://www.zhongchou.com/deal-show/id-%s' %id0
    fp.write(url)
    fp.write('\n')
fp.close()
