import urllib.request
import urllib.parse
import json
import re
import jsonpath


items_list = []
'''

https://rate.taobao.com/feedRateList.htm?auctionNumId=579654818595&userNumId=895000657&currentPageNum=2&pageSize=20&rateType=&orderType=sort_weight&attribute=&sku=&hasSku=true&folded=0&ua=098%23E1hv8pvWvRhvUpCkvvvvvjiPR2FUljtPPLzW1j3mPmPpQj1WRszp0jnvn2Lpzj3PR46CvvyvmnV84V9vaCVjvpvhvvpvv8wCvvpvvUmmRphvCvvvvvvPvpvhMMGvvvhCvvOvCvvvphvEvpCWmhE9vvakfwLOaXTAVADlfXxreEIapbmxfwmK5kx%2F1W1lff8rwZalafmD5iD6BwAQ0f06WeCpqU0HsfUpwZPIAXcBKFyK2ixrAnmK5dyCvm9vvvvvphvvvvvv9krvpvFgvvmm86Cv2vvvvUUdphvUOQvv9krvpv3FkphvC99vvOC0B4yCvv9vvUmssv%2BvoIhCvvswPWrS9nMwznQksHItvpvhvvvvvv%3D%3D&_ksTS=1544255124354_1693&callback=jsonp_tbcrate_reviews_list


'''
def main():
    url = 'https://rate.taobao.com/feedRateList.htm?auctionNumId=579654818595&userNumId=895000657&currentPageNum={}&pageSize=20'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Cookie':'miid=238140751504517940;t=5cfec2633149ae2bbbbb5351f625453b;cna=HuNFFPUU2wMCAXAKa+LNyQIl;thw=cn;hng=CN%7Czh-CN%7CCNY%7C156;tracknick=%5Cu9999%5Cu80A0%5Cu5C06%5Cu519B;lgc=%5Cu9999%5Cu80A0%5Cu5C06%5Cu519B;tg=0;enc=3ZvHFJUqvqj4O%2Be%2FrpFXu0uIw506%2Fylj1n3n6Ix8D9l%2FNTn4v9RUQvs3975%2F4PzlO%2BWqGZ3heqFJI5kqkBczxw%3D%3D;x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0;uc3=vt3=F8dByR6kOfpTg80QO3I%3D&id2=UonfN%2B%2FTjedxfQ%3D%3D&nk2=rOkl5rQkC6s%3D&lg2=WqG3DMC9VAQiUQ%3D%3D;_cc_=UIHiLt3xSw%3D%3D;mt=ci=-1_0;cookie2=1813e56838e0d2d379550ee26045fa16;v=0;_tb_token_=fed8b8531f755; uc1=cookie14=UoTYMhygLdfj5Q%3D%3D;isg=BJ6eK-TyTsJSB519Gji4_tqt7zQg92KxW4yovkgnquE4azxFsOzD6TNNZzdC01rx'
    }
    for i in range(1,1 + 1):
        url_page = url.format(i)
        request = urllib.request.Request(url=url_page, headers=headers)
        json_text = urllib.request.urlopen(request).read().decode()
        # 通过普通格式去除两边的无效字符
        # json_text = json_text.strip('() \n\t\r')
        # 通过正则去除两边的无效字符
        json_text = re.sub(r'\(', '', json_text)
        json_text = re.sub(r'\)', '', json_text)
        # 将json格式字符串转化为python对象
        obj = json.loads(json_text)
        # 抓取评论内容
        # 用户头像、用户名、评论内容、评论时间、手机类型
        # 首先取出comment列表
        comments = obj['comments']
        # print(comments)
        # 遍历这个列表，依次提取每一条评论
        for comment in comments:
            # 找用户头像
            user = jsonpath.jsonpath(comment, '$..user')[0]
            face = 'http:' + user['avatar']
            # 找到用户昵称
            name = user['nick']
            # 评论内容
            ping_content = comment['content']
            # 评论时间
            ping_time = comment['date']
            # 手机信息
            info = jsonpath.jsonpath(comment, '$..sku')[0]
            # 将评论信息保存在字典中
            item = {
                '用户头像':face,
                '用户名':name,
                '评论':ping_content,
                '时间':ping_time,
                '信息':info
            }

            items_list.append(item)
if __name__ == '__main__':
    main()

    string = json.dumps(items_list, ensure_ascii=False)
    # 保存在文件中
    with open('pinglun.txt', 'w', encoding='utf8') as fp:
        fp.write(string)