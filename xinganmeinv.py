import urllib.request
import urllib.parse
from lxml import etree
import os
import time


def handle_request(url, page):
    # 由于第一页和后面的页码不一样，需要进行判断
    if page == 1:
        url = url + '.html'
    else:
        url = url + '_{}.html'.format(str(page))

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }

    request = urllib.request.Request(url=url, headers=headers)
    return request

# 解析内容，下载图片
def download_image(image_src, iamge_title):
    dirpath = 'xinggan'
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    filename = iamge_title + '.jpg'
    filepath = os.path.join(dirpath, filename)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }

    request = urllib.request.Request(url=image_src, headers=headers)
    response = urllib.request.urlopen(request)
    with open(filepath, 'wb') as fp:
        fp.write(response.read())

def parse_content(content):
    tree = etree.HTML(content)
    title_list = tree.xpath('//div[@id="container"]/div/div/a/img/@alt')
    image_list = tree.xpath('//div[@id="container"]/div/div/a/img/@src2')
    # 懒加载
    # 遍历列表img_list，下载图片
    for image_src, image_title in zip(image_list, title_list):
        image_src = str(image_src.replace("_s", ''))
        download_image(image_src, image_title)
        time.sleep(1)

def main():
    url = 'http://sc.chinaz.com/tupian/xingganmeinvtupian'
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))
    for page in range(start_page, end_page + 1):
        request = handle_request(url, page)
        content = urllib.request.urlopen(request).read().decode()
        parse_content(content)
        time.sleep(2)

if __name__ == '__main__':
    main()