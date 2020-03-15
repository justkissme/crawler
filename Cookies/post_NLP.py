import requests,json
import re
url='http://ictclas.nlpir.org/nlpir/index6/getWord2Vec.do'
a="""Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: en,zh;q=0.9,zh-CN;q=0.8
Connection: keep-alive
Content-Length: 35
Content-Type: application/x-www-form-urlencoded
Cookie: JSESSIONID=E424C6A467801A404CDAF15997E5AB07; UM_distinctid=170b0934bed8d1-042991e2afe5e7-3a36550e-1fa400-170b0934bee7ea; CNZZDATA1255328894=1172065609-1583507758-http%253A%252F%252Fictclas.nlpir.org%252F%7C1583507758
Host: ictclas.nlpir.org
Origin: http://ictclas.nlpir.org
Referer: http://ictclas.nlpir.org/nlpir/
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36
X-Requested-With: XMLHttpRequest"""
headers= dict([line.split(": ",1) for line in a.split("\n")])
content = input('请输入你想联想的词:')
data = {'content': content}
res = requests.post(url,headers = headers,data = data)
text = res.text
json = json.loads(text)
list = json['w2vlist']
a=[]
for i in list:
    A=i.split(',')
    a.append(A[0])
print(a)