import requests
url='http://t8.baidu.com/it/u=3571592872,3353494284&fm=79&app=86&f=JPEG?w=1200&h=1290'
res=requests.get(url)
pic=res.content
photo =open('Wind_crawler\\requests\\0-1ppt.jpg','wb')
photo.write(pic)
photo.close()