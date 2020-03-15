from selenium import  webdriver 
import time
driver = webdriver.Chrome('G:\\浏览器\\Chrome\\Application\\chromedriver.exe')
driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php')
time.sleep(2)


name = driver.find_element_by_id('user_login')
name.send_keys('test2333')
pwd = driver.find_element_by_id('user_pass')
pwd.send_keys('123456')
button = driver.find_element_by_name('wp-submit')
button.click()
time.sleep(2)
a = driver.find_elements_by_class_name('entry-title')[1]
a.click()
time.sleep(20)
comment = driver.find_element_by_id('comment')
comment.send_keys('hello world')
button2 = driver.find_element_by_id('submit')
button2.click()
time.sleep(3)

driver.close()