link = 'https://www.xslou.com/yuedu/9356/'

id_list = list(filter(str.isdigit,link))
book_id = ''.join(id_list)
print(type(book_id))
print(book_id)