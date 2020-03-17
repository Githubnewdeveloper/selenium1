from selenium import webdriver

#导入谷歌游览器的插件，文件路径cmd+opt+c
driver = webdriver.Chrome('/Users/apple/Desktop/Programing/pulgin/chromedriver')

#最大化游览器
driver.fullscreen_window()

#打开一个网站
driver.get('http://www.shigeku.org/xlib/gd/ts300/index.htm')

elements = driver.find_elements_by_tag_name('a')
for element in elements:
    if '李白' in element.text:
        element.click()

        break
