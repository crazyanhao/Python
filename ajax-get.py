import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

page = int(input('请输出想要第几页的数据： '))

number = 20
data = {
'start': (page-1)*number,
'limit': number
}
#将字典转化为query_string
query_string = urllib.parse.urlencode(data)
url += query_string

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'
}

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode())