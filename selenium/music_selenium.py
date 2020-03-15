import time 
from selenium import webdriver
driver = webdriver.Chrome('G:\\浏览器\\Chrome\\Application\\chromedriver.exe')

driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html')
time.sleep(2)

#点击加载按钮
button = driver.find_element_by_class_name('js_get_more_hot')
button.click()
time.sleep(2)

#找到评论
comments=driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li')
for comment in comments:
    sweet = comment.find_element_by_tag_name('p')
    print('评论：%s\n ---\n' % sweet.text)

driver.close()