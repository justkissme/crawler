import requests
url='https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
data={'log': 'spiderman',
'pwd': 'crawler334566',
'wp-submit': '登录',
'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
'testcookie': '1'}
login_in=requests.post(url,headers=headers,data=data)
cookies=login_in.cookies
#提取cookies的方法
print(cookies)

url_1='https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
data_1={'comment': input('请输入你想发表的评论:'),
'submit': '发表评论',
'comment_post_ID': '13',
'comment_parent': '0'}
comment = requests.post(url_1,headers=headers,data=data_1,cookies=cookies)
#调用cookies
print(comment.status_code)