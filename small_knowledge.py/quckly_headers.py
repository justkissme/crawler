a='''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Cookie: _userCode_=20191231521156158; _userIdentity_=20191231521156037; homePageType=B; _tt_=E569829E3314ED79F78E2534AA57FBF5; Hm_lvt_6dd1e3b818c756974fb222f0eae5512e=1575357676; yd_cookie=8b8d3224-e113-4b0a9759dfdb9ee50e58c8938dc919b35bc5; DefaultCity-CookieKey=364; DefaultDistrict-CookieKey=0; userId=0; defaultCity=%25E5%25B9%25BF%25E4%25B8%259C%257C364; __utmc=196937584; __utmz=196937584.1575357676.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; strIdCity=China_Beijing; maxShowNewbie=2; _ydclearance=8458845490b50e90cc22046b-28f4-481c-b00c-a01396d3f4e3-1575451319; Hm_lpvt_6dd1e3b818c756974fb222f0eae5512e=1575444117; __utma=196937584.1586138671.1575357676.1575357676.1575444117.2; __utmt=1; __utmt_~1=1; __utmb=196937584.2.10.1575444117
Host: www.mtime.com
Referer: http://www.mtime.com/top/tv/top100/
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'''
headers = dict([line.split(": ",1) for line in a.split("\n")])
print(headers)