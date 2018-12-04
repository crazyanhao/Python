import urllib.request
import re
import requests
import json
# 获取排行榜的类别，总共有十个排行榜需要爬取
url = 'https://www.ximalaya.com/top/'
headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'x_xmly_traffic=utm_source%253A%2526utm_medium%253A%2526utm_campaign%253A%2526utm_content%253A%2526utm_term%253A%2526utm_from%253A; device_id=xm_1543895437163_jp97hbhnbq70ym; Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1543756063,1543757742,1543807229,1543895438; Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070=1543895438',
'Host':'www.ximalaya.com',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode()

item = re.findall('</i><a href="/(.*?)/top/"><span class="B5x">', html)
url_item = 'https://www.ximalaya.com/revision/getRankList?code={}'
for i in item:
    url1 = url_item.format(i)
    print(url1)
    r1 = requests.get(url1, headers = headers)
    ret1 = r1.content.decode()
    c1 = json.loads(ret1)
    b1 = c1['data']['albums']

    start_url = 'https://www.ximalaya.com/revision/play/album?albumId={0}&pageNum={1}&sort=1&pageSize=30'


    for i in b1:
            v = i['id']
            for i in range(50):
                try:
                    url = start_url.format(v,i+1)
                    r = requests.get(url, headers = headers)
                    ret = r.content.decode()
                    print(ret)
                    c = json.loads(ret)
                    b = c['data']['tracksAudioPlay']
                    for i in b:
                        name = i['trackName']
                        src = i['src']
                        print(name,
                              src)
                        with open('img/%s.m4a'% name, 'wb') as f:
                            r = requests.get(src)
                            f.write(r.content)
                except:
                    print('获取失败')