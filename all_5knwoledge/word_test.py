import requests
link = requests.get('https://www.shanbay.com/api/v1/vocabtest/category/')
js_link = link.json()
#让用户选择自己想测的词库,输入数字编号.int()来转换数据类型
num_choice = int(input('''请输入你选择的词库编号,按Enter确认
1,GMAT 2,考研 3,高考, 4,四级 5,六级
6,英专 7,托福 8,GRE   9,雅思 10,任意
'''))
#获得测单词的网址
ciku = js_link['data'][num_choice-1][0]
url_test = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+ciku
#获得单词
test = requests.get(url_test)
# print(test.status_code)
datas = test.json()['data']
print(type(datas))
all_word={}
#列出所有单词
for i,content in enumerate(datas):
    content = content['content']
    print(str(i+1) + ':' +content)
    all_word[i+1] = content
print(all_word)
    

#输入你认识的单词序号
know_choice = list(input('请选择你认识的单词,输入数字,用逗号分隔:').split(','))
##创建一个认识的单词字典
know_word=[]
for know_num in know_choice:
    know_word.append(all_word[int(know_num)])#回答正确就加入到know_word里
print('这些单词都是你认识的:')
print(know_word)
print('现在我们来检测下你是否掌握了这些知识,请选择每个单词正确的答案,输入序号:'
ranks=datas[int(num2)-1]['definition_choices']
#     print('A'+ranks[0]['definition'])
#     print('B'+ranks[1]['definition'])
#     print('C'+ranks[2]['definition'])
#     print('D'+ranks[3]['definition'])    
#     right_num = input('请输入单词'+all_word[int(num2)]+'正确选项:')
     
    
     






