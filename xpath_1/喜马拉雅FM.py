
import requests
import json
url_item = 'https://www.ximalaya.com/revision/getRankList?code={}'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
item = ['xiangsheng','yinyue','lishi','qinggan','renwen','yule','waiyu','ertong','youshengshu','jiaoyu']
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
                        # with open('img/%s.m4a'% name, 'wb') as f:
                        #     r = requests.get(src)
                        #     f.write(r.content)
                except:
                    print('获取失败')