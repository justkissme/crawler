import requests
import json
session = requests.session()
#用requests.session()创建session对象，帮我们保持了cookies
url='https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
data={'log':'spiderman',
'pwd': 'crawler34566',
'wp-submit': '登录',
'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
'testcookie': '1'}
session.post(url,headers=headers,data=data)
cookies_dict=requests.utils.dict_from_cookiejar(session.cookies)
print(type(cookies_dict))
#将cookies转换成字典
cookies_str = json.dumps(cookies_dict)
print(type(cookies_str))
#调用json模块的dumps函数，把cookies从字典转成字符串
f=open('Wind_crawler\\Cookies\\session.txt','w')
f.write(cookies_str)
f.close()
#保存转换成字符串的cookies
# url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
# #想要评论的文章网址
# data_1={'comment': input('请输入你想要发表的评论：'),
# 'submit': '发表评论',
# 'comment_post_ID': '13',
# 'comment_parent': '0'
# }
# comment=session.post(url_1,headers=headers,data=data_1)
# print(comment)