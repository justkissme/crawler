import requests
import openpyxl
wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='zhihu'
sheet.append(['文章名','链接'])
url='https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
offset=0
while 1:
    params={'include': 'data[*].comment_count,suggest_edit,is_normal,     thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
        'offset': str(offset),
        'limit': '10',
        'sort_by': 'voteups'}
    res=requests.get(url,headers=headers,params=params)
    json=res.json()
    for data in json['data']:
        title=data['title']
        href=data['url']
        print(title)
        sheet.append([title,href])
        offset=offset+10
    if offset>30:
        break
    
wb.save('Wind_crawler\\all_5knwoledge\\all_5knowledge.xlsx')    

