import requests
url='https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html'
res=requests.get(url)
html=res.content
with open('Wind_crawler\\HTML\\html_download.html','wb') as f:
    f.write(html)
