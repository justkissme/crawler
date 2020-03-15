import requests,json
session = requests.session()
headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
try:
#如果能读取cookies文件，执行以下代码，跳过except代码，不用登陆就能发表评论
    cookies_txt=open('Wind_crawler\\Cookies\\session.txt','r')
    cookies_dict=json.loads(cookies_txt.read())
    #将字符串转换成字典
    cookies=requests.utils.cookiejar_from_dict(cookies_dict)
    #将字典转换成cookies本来的格式
    session.cookies = cookies 
    #获取cookies
except FileNotFoundError:
#如果读不到cookies文件，报错，执行以下代码，重新获取cookies
    url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
    #登录的网址。
    data = {'log': 'spiderman',
            'pwd': 'crawler34566',
            'wp-submit': '登录',
            'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
            'testcookie': '1'}
    #登录的参数。
    session.post(url, headers=headers, data=data)
    #在会话下，用post发起登录请求。

    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    #把cookies转化成字典。
    cookies_str = json.dumps(cookies_dict)
    #调用json模块的dump函数，把cookies从字典再转成字符串。
    f = open('Wind_crawler\\Cookies\\session.txt', 'w')
    #创建名为cookies.txt的文件，以写入模式写入内容
    f.write(cookies_str)
    #把已经转成字符串的cookies写入文件
    f.close()
    #关闭文件
url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
#文章的网址。
data_1 = {
'comment': input('请输入你想评论的内容：'),
'submit': '发表评论',
'comment_post_ID': '13',
'comment_parent': '0'
}
#评论的参数。
comment = session.post(url_1,headers=headers,data=data_1)
#在创建的session下用post发起评论请求，放入参数：文章网址，请求头和评论参数，并赋值给comment。
print(comment.status_code)
#打印comment的状态码    