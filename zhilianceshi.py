''''' 
    智联招聘——爬虫源码————2018.11 
'''
import requests
import re
import time
from lxml import etree
import csv
import random

fp = open('智联招聘.csv','wt',newline='',encoding='UTF-8')
writer = csv.writer(fp)
'''''地区，公司名，学历，岗位描述，薪资，福利，发布时间，工作经验，链接'''
writer.writerow(('职位','公司','地区','学历','岗位','薪资','福利','工作经验','链接'))

def info(url):
    res = requests.get(url)
    u = re.findall('<meta name="mobile-agent" content="format=html5; url=(.*?)" />', res.text)

    if len(u) > 0:
        u = u[-1]
    else:
        return

    u = 'http:' + u

    headers ={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
    }

    res = requests.get(u,headers=headers)
    selector = etree.HTML(res.text)

    # # 岗位名称
    title = selector.xpath('//*[@id="r_content"]/div[1]/div/div[1]/div[1]/h1/text()')
    # # 岗位薪资
    pay = selector.xpath('//*[@id="r_content"]/div[1]/div/div[1]/div[1]/div[1]/text()')
    # # 工作地点
    place = selector.xpath('//*[@id="r_content"]/div[1]/div/div[1]/div[3]/div[1]/span[1]/text()')
    # # 公司名称
    companyName = selector.xpath('//*[@id="r_content"]/div[1]/div/div[1]/div[2]/text()')
    # # 学历
    edu = selector.xpath('//*[@id="r_content"]/div[1]/div/div[1]/div[3]/div[1]/span[3]/text()')
    ea = ''
    for edu_a in edu:
        if edu_a.strip().replace('\n','') == '':
            continue
        else:
            ea = edu_a.strip().replace('\n','')
    # # 福利
    walfare = selector.xpath('//*[@id="r_content"]/div[1]/div/div[3]/span/text()')
    walfare_a = ''
    for wf in walfare:
        walfare_a = walfare_a + wf + ','
    walfare_a.rstrip(',')
    # # 工作经验
    siteUrl = res.url
    workEx = selector.xpath('//*[@id="r_content"]/div[1]/div/div[1]/div[3]/div[1]/span[2]/text()')
    workexp = ''
    for we in workEx:
        if we.strip().replace('\n','') == '':
            continue
        else:
            workexp = we.strip().replace('\n','')
    # # 岗位详细
    comment = selector.xpath('//*[@id="r_content"]/div[1]/div/article/div/p/text()')
    a = ''
    for commm in comment:
        b = commm.replace('\n','').replace('\\xa','')
        a = a + b
    writer.writerow((title[0], companyName[0], place[0], ea, a, pay[0], walfare_a, workexp, siteUrl))
    print(title, companyName, place, edu, comment, pay, walfare, workEx, siteUrl)

def infoUrl(url):
    res = requests.get(url)
    selector = res.json()
    code = selector['code']
    if code == 200:
        data = selector['data']['results']
        for i in data:
            href = i['positionURL']
            info(href)
            time.sleep(random.randrange(1,4))

if __name__ == '__main__':
    key = '爬虫工程师'

    url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=653&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=' + key + '&kt=3&lastUrlQuery=%7B%22pageSize%22:%2260%22,%22jl%22:%22489%22,%22kw%22:%22%E5%A4%A7%E6%95%B0%E6%8D%AE%22,%22kt%22:%223%22%7D'
    infoUrl(url)

    urls = ['https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=653&kw='.format(i*60)+key+'&kt=3&lastUrlQuery=%7B%22p%22:{},%22pageSize%22:%2260%22,%22jl%22:%22489%22,%22kw%22:%22java%22,%22kt%22:%223%22%7D'.format(i) for i in range(1,50)]
    for url in urls:
        infoUrl(url) 
