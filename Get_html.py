def get_html(filename):
    #url = 'http://www.8btc.com/vc'
    f1 = open('tim.txt', 'w')
    f2 = open('money.txt', 'w')
    f3 = open('address.txt', 'w')
    for url in open(filename,'r+',encoding='utf-8'):
        #id0 = url.strip().split('/')[-1]
        url = url.strip()
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'www.8btc.com',
            'Referer': 'http://www.cnvd.org.cn/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        #print(response.status_code)
        html = response.content

def get_proj_html(filename):
    f = open('%s.txt' % filename,'r+',encoding='utf-8')
    result = f.readlines()
    f.close()
    results = [b[:-1] for b in result]
    print(len(results))
    for url in results:
        id0 = url.split('/')[-2]
        headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0')
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        html = urllib.request.urlopen(url).read()
        time.sleep(5)
        filename = "%s.txt" % id0
        f = open(filename, "wb")
        f.write(html)
        f.close()
    print('This process is ending!')
#get_proj_html('update_url')
