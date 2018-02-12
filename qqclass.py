import urllib.request
from bs4 import BeautifulSoup
f = open('qqclass.txt','w',encoding='utf8')
for i in range(1,3):
    url = "https://ke.qq.com/course/list?mt=1001&st=2003&tt=3022&page=%d" %i
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'lxml')
    base_info = soup.find('div',{'class':'market-bd'})
    for href in base_info.find_all('a',{'class':'item-img-link'}):
        url1 = 'https:' + href.get('href').strip()
        if url1.find('package') != -1:continue
        #https://ke.qq.com/course/121211
        #print(url1)
        id0 = url1.split('/')[-1]
        #print(id0)
        html = urllib.request.urlopen(url1).read()
        #html = urllib2.urlopen(url).read()
        soup1 = BeautifulSoup(html,'lxml')
        right_info = soup1.find('div',{'class':'text-right'})
        title = right_info.find('span',{'class':'title-main'}).text.strip()
        cont_info = right_info.find('div',{'class':'class-content-list'})
        class_cate = cont_info.find('h2').text.strip()
        class_date = cont_info.find('p').text.strip()
        price_info = right_info.find('p',{'class':'course-price-info'}).text.strip()
        block_info = soup1.find('div',{'class':'aside-blocks'})
        tree_info = block_info.findAll('li')
        levelDegree = tree_info[0].find('span').text.strip()
        classNum = tree_info[1].find('span').get('data-num')
        stuNum = tree_info[2].find('span').get('data-num')
        class_info = id0+'\t'+title+'\t'+class_cate+'\t'+class_date+'\t'+price_info+'\t'+levelDegree+'\t'+classNum+'\t'+stuNum
        f.write(class_info)
        f.write('\n')
f.close()
