import urllib.request
import urllib.parse
import re
import time

def handle_request(url, page = None):
    if page != None:
        url = url + str(page) + '.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }
    request = urllib.request.Request(url, headers=headers)
    return request

def get_text(a_href):
    # 调用函数构建请求对象
    request = handle_request(a_href)
    # 发送请求，获取响应
    content = urllib.request.urlopen(request).read().decode()
    # 解析内容
    pattern = re.compile(r'<div class="neirong">(.*?)</div>', re.S)
    lt = pattern.findall(content)
    text = lt[0]
    # 写个正则，将内容里面所有的图片标签全部清空
    pat = re.compile(r'<img .*?>')
    pat.sub('', text)
    return text

def parse_content(content):
    pattern = re.compile(r'<h3><a href="(/lizhi/qianming/\d+\.html)">(.*?)</a></h3>')
    # 返回的lt是个列表，列表中的元素都是元组，元组中第一个元素就是正则中第一个小括号匹配到的内容，元组总第二个元素就是正则中第二个小括号匹配的内容
    lt = pattern.findall(content)
    for href_title in lt:
        # 获取内容链接
        a_href = 'http://www.yikexun.cn' + href_title[0]
        # 获取标题
        a_title = href_title[-1]
        title = a_title.strip('<b></b>')
        # 像a_href发送请求，获取响应内容
        text= get_text(a_href)
        # 写入html文件中
        string = '<h1>%s</h1>%s' % (title, text)
        with open('lizhi.html', 'a',encoding='utf8') as fp:
            fp.write(string)
        time.sleep(2)

def main():
    start_page = int(input('请输入起始页码： '))
    end_page = int(input('请输入结束页码： '))
    url = 'http://www.yikexun.cn/lizhi/qianming/list_50_'
    for page in range(start_page, end_page + 1):
        # 根据url和page生成指定的request
        request = handle_request(url, page)
        # 发送请求
        content = urllib.request.urlopen(request).read().decode()
        # 解析内容
        parse_content(content)
if __name__ == '__main__':
    main()