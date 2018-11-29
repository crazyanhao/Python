import requests
from lxml import etree

# 面向对象设计模式
class Spider(object):
    def __init__(self):
        self.offset = 1
    def start_work(self):
        for self.offset in range(1,224):
            print('正在爬取第%d页....' % self.offset)
            response = requests.get(url = 'https://ibaotu.com/shipin/7-0-0-0-0-' + str(self.offset) + '.html')
            html = response.text
            html = etree.HTML(html)
            video_src = html.xpath('//div[@class="video-play"]/video/@src')
            video_title = html.xpath('//span[@class="video-title"]/text()')
            # 使得获取完整的视频连接而不是被压缩过的视频连接
            real_src = []
            for i in video_src:
                current_src = i[:-8]
                real_src.append(current_src)
            self.write_file(real_src, video_title)
    def write_file(self, real_src, video_title):
        for src, title in zip(real_src, video_title):
            response = requests.get('http:' + src)
            filename = title + '.mp4'
            print('正在抓取%s' % filename)
            with open(filename, 'wb') as f:
                f.write(response.content)
spider = Spider()
spider.start_work()
