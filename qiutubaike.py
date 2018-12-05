import urllib.request
import urllib.parse
import re
import os
import time
def handle_request(url, page):
    url = url + str(page) + '/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }
    request = urllib.request.Request(url, headers=headers)
    return request
def download_image(content):
    pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)" alt=".*?',re.S)
    lt = re.findall(pattern,content)
    #遍历列表，依次下载图片
    for image_src in lt:
        # 先处理image_src
        image_src = 'https:' + image_src
        #创建文件夹
        dirname = 'qiutu'
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        # 图片名字
        filename = image_src.split('/')[-1]
        filepath = dirname + '/' + filename
        print('%s图片正在下载......'% filename)
        # 发送请求 下载图片
        urllib.request.urlretrieve(image_src, filepath)
        print('%s图片下载完毕......'% filename)
        time.sleep(1)
def main():
    url = 'https://www.qiushibaike.com/pic/page/'
    start_page = int(input('请输入想下载的起始页码： '))
    end_page = int(input('请输入想下载的结束页码： '))
    for page in range(start_page, end_page + 1):
        print('第%s页开始下载......'% page)
        # 生成请求对象
        request = handle_request(url, page)
        # 发送请求对象，获取响应内容
        content = urllib.request.urlopen(request).read().decode()
        # 解析内容，提取所有图片链接，下载图片
        download_image(content)
        print('第%s页下载完毕......' % page)
        print()
        print()
        time.sleep(2)
if __name__ == '__main__':
    main()