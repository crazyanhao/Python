import urllib.request
import urllib.parse
import os
url = 'http://tieba.baidu.com/f?ie=utf-8&'
#输入贴吧名称，输入起始页码，输入结束页码，然后在当前文件夹中创建一个以吧名为名字的文件夹，里面是每一页的html内容，文件名是 吧名_page.html
name = input('请输入您想查询的贴吧： ')
page_start = int(input('请输入起始页码： '))
page_end = int(input('请输入结束页码： '))
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
# 创建文件夹
if not os.path.exists(name):
    os.mkdir(name)

# 利用循环依次爬取每一页数据
for page in range(page_start, page_end + 1):
    # page为当前页
    # 拼接url的过程
    data = {
        'kw': name,
        'pn': (page - 1)*50
    }
    data = urllib.parse.urlencode(data)
    #生成指定的url
    eve_url = url + data
    #发请求
    request = urllib.request.Request(eve_url,headers=headers)
    print('第%s页开始下载......'% page)
    response = urllib.request.urlopen(request)
    #有了响应可以写文件了
    # 生成文件名
    filename = name + '_' + str(page) + '.html'
    # 拼接文件路径
    filepath = name + '/' + filename

    # 写内容
    with open(filepath, 'wb') as f:
        f.write(response.read())
    print('第%s页结束下载......' % page)