#导入网页司机

from selenium import webdriver

#导入谷歌游览器的插件，文件路径cmd+opt+c
driver = webdriver.Chrome('/Users/apple/Desktop/Programing/pulgin/chromedriver')

#最大化游览器
driver.fullscreen_window()

#打开一个网站
driver.get('http://www.google.com')
