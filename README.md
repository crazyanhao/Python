# Python  
个人python学习之旅......  
一、2018年11月29日18:45:34 利用requests、etree模块进行视频爬取,使用xpath。  
二、2018年11月29日20:52:36 添加了一个2048的小游戏。  
三、2018年11月30日22:34:24 添加了简单的99乘法表和windows的一个小时钟。  
四、2018年12月1日23:46:14 补充了一个来自网课的爬虫。爬取内容是喜马拉雅排行榜的音频，最终希望实现爬取全排行榜（免费）的音频，目前能爬取一个排行榜的所有专辑里的音频，代码还很粗糙，有待加强！  
五、2018年12月2日15:57:49 更新了喜马拉雅的爬虫，现在可以爬取所有（10个）排行榜的音频，但一些关键词的获取还需要补充。更新后的文件在xpath_1文件夹内。（被误操作git clean -f误删了）  
六、2018年12月4日15:29:09 喜马拉雅排行榜初步完成，使用正则表达式匹配关键词并构成列表，但仍有不足之处，例如很多循环都是无用循环、也没记录功能，以后有机会补充并完善。本次更新代码：day3.py......  
七、2018年12月4日20:54:20 更新了三个小爬虫，爬取html数据，ajax下的json数据。第一个为豆瓣电影的影片排行榜数据，文件名为ajax-get.py......第二个为肯德基的餐厅定位搜索，可以获得不同城市KFC餐厅的信息，文件名为ajax-post.py......第三个为百度贴吧的信息，可以搜索吧名和具体页码，并创建文件夹归类，将每一页保存到本地，文件名为tieba.py......  
八、2018年12月5日22:23:05 更新了两个实战爬虫。第一个爬取网站为糗事百科，把网站内图片保存到本地一个新建文件夹内，代码为：qiushibaike.py......第二个是爬取一点点语录网内的励志名言，通过每篇文章的标题进入，获取每篇文章的标题和具体内容，并保存在本地的html文件中，代码为yikexun.py......本次两个实战爬虫均用到了正则表达式。  
九、2018年12月6日21:36:14 学习了bs4的使用以及lxml解析器，bs4的使用方法已经了解。更新了一个用xpath爬取智联招聘的岗位信息，工作地点是杭州，职位是爬虫工程师，并把内容保存在本地csv文件中，文件名为zhilianceshi.py......  
十、2018年12月9日15:00:47 了解了jsonpath和selenium，爬取了一个图片网站和淘宝的评论信息。实现过程中中发现天猫商城和淘宝的爬取方式有一定的区别，可能天猫的网站更加强大。另外由于phantomjs与selenium不再合作，以后均使用headless chrome进行操作。文件名为xinganmeinv.py和taobao.py......  
十一、2018年12月9日21:52:26 更新了爬取8684杭州公交线路的代码，保存到本地。使用requests解析网页，xpath提取数据。文件名为hangzhougongjiao.py......  
十二、2018年12月10日15:03:50  更新的通过人工输入验证码的方式登录古诗文网，十分影响效率。文件名为logingushi.py......
