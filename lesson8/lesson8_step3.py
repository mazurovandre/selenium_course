from selenium import webdriver
import math, time

link = "http://suninjuly.github.io/selects1.html"
# link = "http://suninjuly.github.io/selects2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('num1').text
    y = browser.find_element_by_id('num2').text
    sum = 'option[value="' + str(int(x) + int(y)) + '"]'

    browser.find_element_by_id('dropdown').click()
    browser.find_element_by_css_selector(sum).click()

    browser.find_element_by_css_selector('button[type=submit]').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
