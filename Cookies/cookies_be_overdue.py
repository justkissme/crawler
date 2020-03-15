import requests,json
session = requests.session()
#创建会话
headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
#添加请求头，避免被反爬虫
try:
#如果能读取到cookies文件，执行以下代码
    cookies_txt = open('Wind_crawler\\Cookies\\session.txt','r')
    cookies_dict=json.loads(cookies_txt)
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    session.cookies = cookies
    #获取会话下的cookies

except FileNotFoundError:
#如果读不到cookies文件，报错，执行以下代码
    url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
    data= {'log': input('请输入你的账号:'),
            'pwd': input('请输入你的密码:'),
            'wp-submit': '登录',
            'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
            'testcookie': '1'}
    #登陆的参数
    session.post(url,headers=headers,data=data)  
    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)   
    cookies_str=json.dumps(cookies_dict)
    f=open('Wind_crawler\\Cookies\\session.txt','w')
    f.write(cookies_str)
    f.close()


url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
data_1 = {
'comment': input('请输入你想评论的内容：'),
'submit': '发表评论',
'comment_post_ID': '13',
'comment_parent': '0'
}
#评论的参数
session.post(url_1,headers=headers,data=data_1)