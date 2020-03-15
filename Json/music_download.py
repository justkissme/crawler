import requests
import openpyxl

#Excel创建
wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='music_infos'
sheet.append(['歌名','专辑','时长','链接'])
url='https://c.y.qq.com/soso/fcgi-bin/client_search_cp?'
params={'ct': '24',
'qqmusic_ver': '1298',
'new_json': '1',
'remoteplace': 'txt.yqq.song',
'searchid': '68887358482356764',
't': '0',
'aggr': '1',
'cr': '1',
'catZhida': '1',
'lossless': '0',
'flag_qc': '0',
'p': '1',
'n': '10',
'w': '周杰伦',
'g_tk': '1108539358',
'loginUin': '2294776060',
'hostUin': '0',
'format': 'json',
'inCharset': 'utf8',
'outCharset': 'utf-8',
'notice': '0',
'platform': 'yqq.json',
'needNewCode': '0'}
headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
res=requests.get(url,headers=headers,params=params)
json=res.json()
lists=json['data']['song']['list']
for list in lists:
    name=list['name']
    time=list['interval']
    m,s=divmod(time,60)
    interval=('%02d:%02d' % (m,s))#将秒数转换成分钟
    html='https://y.qq.com/n/yqq/song/'+list['mid']+'.html'
    album=list['album']['name']
    sheet.append([name,album,interval,html])
wb.save('Wind_crawler\\Json\\music_download.xlsx')
wb.close()
    
  
    
    