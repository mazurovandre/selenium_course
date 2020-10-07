from selenium import webdriver
import os, time

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

first_name = browser.find_element_by_name('firstname')
first_name.send_keys('Name')
last_name = browser.find_element_by_name('lastname')
last_name.send_keys('Surname')
email = browser.find_element_by_name('email')
email.send_keys('hu@ya.com')

element = browser.find_element_by_id('file')
# путь до файла и его название будут уже другие
file = os.path.join('/Users/mazurovandre/Desktop', 'history.txt')
element.send_keys(file)

button = browser.find_element_by_tag_name('button')
button.click()

time.sleep(5)
browser.quit()