import urllib.request    #urllib2
from bs4 import BeautifulSoup
from lxml import *

f = open('html.txt','r+')
result = f.read()
f.close()
soup = BeautifulSoup(result,'html.parser')

img_info = soup.find('div',{'class':'sousuoListBox'})
img = img_info.find_all('img')
image = [x.get('src') for x in img]
#print(image)
def save_file(path, file_name, data):
    file = open(path+file_name,"wb")
    file.write(data)
    file.flush()
    file.close()
    
i = 0
for url in image:
    im = urllib.request.urlopen(url).read()#im = urllib2.urlopen(url).read()
    save_file('C:/html/',str(i)+'.jpg',im)
    i += 1
