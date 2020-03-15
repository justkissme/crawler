import requests
url='https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?'
headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
HotComment=open('Wind_crawler\\Json\\common_download.txt','wb')
for i in range(5):
    params={'g_tk': '1108539358',
    'loginUin': '2294776060',
    'hostUin': '0',
    'format': 'json',
    'inCharset':'utf8',
    'outCharset': 'GB2312',
    'notice': '0',
    'platform':' yqq.json',
    'needNewCode': '0',
    'cid': '205360772',
    'reqtype': '2',
    'biztype': '1',
    'topid': '102065756',
    'cmd': '6',
    'needmusiccrit': '0',
    'pagenum': str(i),
    'pagesize': '15',
    'lasthotcommentid':'song_102065756_1922634187_1466696717',
    'domain': 'qq.com',
    'ct': '24',
    'cv': '10101010'}
    res=requests.get(url,params=params,headers=headers)
    comments_json=res.json()
    comments=comments_json['comment']['commentlist']
    for comment in comments:
        nick=comment['nick']
        hot_comment=comment['rootcommentcontent']
        HotComment.write(str.encode(nick + '    ' + hot_comment+'\n'))
        HotComment.write(str.encode('---------------------------\n'))
HotComment.close()