from selenium import  webdriver 
import time

driver = webdriver.Chrome('G:\\浏览器\\Chrome\\Application\\chromedriver.exe')
driver.get('https://qzone.qq.com/')
time.sleep(5)
#此处需要切换到元素所在的frame下
driver.switch_to_frame('login_frame')
gin=driver.find_element_by_id('switcher_plogin')
gin.click()
time.sleep(3)
name = driver.find_element_by_name('u').send_keys('2294776060')
pwd = driver.find_element_by_name('p').send_keys('qnmlgb2333')
button = driver.find_element_by_id('login_button').click()
time.sleep(20)




driver.close()