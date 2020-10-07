from selenium import webdriver
import time, math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name('button')
    button.click()

    prompt = browser.switch_to.alert
    prompt.accept()

    x = browser.find_element_by_id('input_value').text
    answer = calc(x)
    browser.find_element_by_id('answer').send_keys(answer)
    button = browser.find_element_by_tag_name('button')
    button.click()

    result = browser.switch_to.alert.text.split(': ')[-1]

    print('Result: ' + result)
finally:
    time.sleep(5)
    browser.quit()