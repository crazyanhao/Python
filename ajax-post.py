import urllib.request
import urllib.parse

post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
city = input('请输入要查询的城市： ')
page = input('请输入要查询的页码： ')
size = input('请输入要多少条信息： ')

formdata = {
    'cname':city,
    'pid':'',
    'pageIndex':page,
    'pageSize':size
}

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

request = urllib.request.Request(url=post_url,headers=headers)
#为什么最后还要encode一下?????
formdata = urllib.parse.urlencode(formdata).encode()

response = urllib.request.urlopen(request, data=formdata)
print(response.read().decode())