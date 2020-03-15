# 本地Chrome浏览器设置方法
from selenium import  webdriver 
import time
driver = webdriver.Chrome('G:\\浏览器\\Chrome\\Application\\chromedriver.exe')
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)

teacher = driver.find_element_by_id('teacher')
teacher.send_keys('你真帅')
assistant = driver.find_element_by_id('assistant')
assistant.send_keys('琦玉老师')
button=driver.find_element_by_class_name('sub')
button.click()
time.sleep(3)
driver.close()