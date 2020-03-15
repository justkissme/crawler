import requests,json
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data ={'i': input('你想翻译什么啊:'),
'from': 'AUTO',
'to': 'AUTO',
'smartresult': 'dict',
'client': 'fanyideskweb',
'salt': '15834926828275',
'sign': '4727f06e82e880f57048a3af5f49a32b',
'ts': '1583492682827',
'bv': 'aebb3706172bf86d13745c023f705992',
'doctype': 'json',
'version': '2.1',
'keyfrom': 'fanyi.web',
'action': 'FY_BY_REALTlME'}


b="""Host: fanyi.youdao.com
Origin: http://fanyi.youdao.com
Referer: http://fanyi.youdao.com/
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"""
headers = dict([line.split(": ",1) for line in b.split("\n")])
res = requests.post(url,headers = headers,data=data )
json = res.json()
print(json['translateResult'][0][0]['tgt'])

