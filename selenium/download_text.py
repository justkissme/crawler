from selenium import  webdriver 
import time
from bs4 import BeautifulSoup
driver = webdriver.Chrome('G:\\浏览器\\Chrome\\Application\\chromedriver.exe')
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)

teacher = driver.find_element_by_class_name('teacher').send_keys('刘洋洋')
assistant = driver.find_element_by_class_name('assistant').send_keys('刘洋洋')
button = driver.find_element_by_class_name('sub').click()

time.sleep(3)
#用selenium方法提取文本
# contents = driver.find_elements_by_class_name('content')
# for content in contents:
#     print(content.text)

#用beautifulsoup方法提取文本
text = driver.page_source
print(type(text))
bs = BeautifulSoup(text,'html.parser')
contents = bs.find_all('div',class_='content')
print(type(contents))
for content in contents:
    print(type(content))
    print(content.text)


driver.close()
