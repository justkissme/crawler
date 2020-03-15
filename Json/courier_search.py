import requests
import random
cookie = input('请输入网页的cookies值:')
courierType = input('请输入快递类型(拼音):')
courierID = input('请输入你想查询的快递单号:')
url='https://www.kuaidi100.com/query?'

headers ={'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en,zh;q=0.9,zh-CN;q=0.8',
'Connection': 'keep-alive',
'Cookie': cookie,
'Host': 'www.kuaidi100.com',
'Referer': 'https://www.kuaidi100.com/',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'}
a= random.random(0,9999)
params = {'type': courierType,
'postid': courierID,
'temp': '0.758836685259' + str(a),
'phone':''
}
res = requests.get(url,headers=headers,params=params )
print(res.text)
# json = res.json()
# print(json['data'])