import openpyxl
#引用openpyxl
wb=openpyxl.Workbook()
#创建新的工作薄对象，W大写，要加括号
sheet=wb.active
#获取活动表,不加括号
sheet.title = 'hello world'
#表格命名
sheet['A1'] = '星期'
#在A1单元格中写入‘星期’
row = ['周一','周二','周三']
sheet.append(row)
#写入一行内容
rows=(['早上','中午','晚上'],['早上','中午','晚上'])
for i in rows:
    sheet.append(i)
#写入多行内容
wb.save('Wind_crawler\\Excel\\Excel_learn.xlsx')
#保存文件