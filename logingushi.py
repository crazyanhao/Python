import requests
from bs4 import BeautifulSoup
import urllib.request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',

}

def download_code(s):
    url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
    r = s.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    # 得到图片链接，下载图片到本地
    image_src = 'https://so.gushiwen.org' + soup.find('img', id="imgCode")["src"]
    # print(image_src)
    r_image = s.get(image_src, headers=headers)
    with open('code.png', 'wb')as fp:
        fp.write(r_image.content)

    # 查找表单所需要的两个参数
    __VIEWSTATE = soup.find('input', id="__VIEWSTATE")["value"]
    __VIEWSTATEGENERATOR = soup.find('input', id="__VIEWSTATEGENERATOR")["value"]
    return __VIEWSTATE, __VIEWSTATEGENERATOR

def login(view, viewg, s):
    post_url = 'https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
    # 提示用户输入验证码
    code = input('哥们，麻烦输入验证码：')
    formdata = {
        '__VIEWSTATE': view,
        '__VIEWSTATEGENERATOR': viewg,
        'from': 'http://so.gushiwen.org/user/collect.aspx',
        'email': '1090509990@qq.com',
        'pwd': '123456',
        'code': code,
        'denglu': '登录'
    }
    r = s.post(url=post_url, headers=headers, data=formdata)

    with open('gushi.html', 'w', encoding='utf8') as fp:
        fp.write(r.text)

def main():
    # 创建会话
    s = requests.Session()
    # 下载验证码到本地
    view, viewg = download_code(s)
    # 向post地址发送请求
    login(view, viewg, s)

if __name__ == '__main__':
    main()