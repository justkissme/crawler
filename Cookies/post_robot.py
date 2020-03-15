import requests,json
def robot(spoken):  
    url='https://api.ownthink.com/bot?' 
    params = {'appid': 'xiaosi',
        'spoken':spoken}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
    res = requests.get(url,headers=headers,params=params)
    re_text = json.loads(res.text)
    print('人工智障:'+re_text['data']['info']['text'])
def begin():
    print('欢迎来到你的月亮我的心,我是人见人爱,花见花开的翠花呀,对我说点什么吧主人,如果没什么说的就输入\'滚\'吧')
    while True:
        spoken=input('我滴个神:')
        if spoken =='滚':
            print('人工智障:好嘞')
            break
        else:
            robot(spoken)
begin()