import requests,re
#得到网页源代码
url = 'https://movie.douban.com/top250'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}#请求头,防止反爬虫
res = requests.get(url,headers=headers)
content = res.text.replace(' ','').replace('\n','')#将网页源代码空格和换行符替换掉
# print(content) #修改后的网页源代码
#开始正则匹配
all_tags = re.findall('.*grid_view.*?(<li>.*</li>)',content)[0]
# print(all_tags)
movie_tags = re.findall('<li>.*?</li>',all_tags)
movie_information = []
for movie_tag in movie_tags:
    #提取电影名字
    movie_name = re.findall('.*?class="title">(.*?)<',movie_tag)[0]
    # print(movie_name)

    #提取上映时间.地点和分类
    other = re.findall('.*?class="bd".*?<br>(.*?)</p>.*',movie_tag)[0]
    # print(other)
    #从other中提取上映时间   
    release_data = int(re.findall('\d+',other)[0])
    #提取上映地点
    release_place = re.findall('.*?/(.*?)/',other)[0].replace('&nbsp;','')
    # # #有疑问
    # place = re.search('.*?;(/w.*/w)?&.*',release_place)
    # print(place.group())

    #提取电影分类
    release_category = re.findall('.*;(.*)',other)[0]
    # print(release_category)
    #提取电影评分
    movie_rate = float(re.findall('.*?rating_num.*?>(.*?)<.*?',movie_tag)[0])
    # print(movie_rate)

    movie_information.append((movie_name,release_data,release_place,release_category,movie_rate))
print(movie_information)

    



