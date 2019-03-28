#导入网页司机

from selenium import webdriver

import time

#导入谷歌游览器的插件，文件路径cmd+opt+c
driver = webdriver.Chrome('/Users/apple/Desktop/Programing/pulgin/chromedriver')

#最大化游览器
driver.fullscreen_window()

#打开一个网站
driver.get('http://www.baidu.com')

#模拟人类的鼠标点击动作
#先要在Beatiful Soup中找到link的名字，注意只有element不是列表的才能点击
#driver.find_element_by_name("tj_trnews").click()

#直接用链接上的文字（网页上的）
#driver.find_element_by_link_text('hao123').click()

#使用网页检查中的小箭头可以快速定位元素
driver.find_element_by_id('kw').send_keys('ddos')
#自动搜索
driver.find_element_by_id('su').click()
#让它睡两秒钟，不然太快就关掉了
time.sleep(3)

driver.quit()