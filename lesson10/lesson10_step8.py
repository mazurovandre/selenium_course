from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    book = browser.find_element_by_id("book")
    browser.execute_script("return arguments[0].scrollIntoView(true);", book)

    # говорим Selenium проверять в течение 12 секунд, пока цена не станет $100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book.click()
    solve = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", solve)

    x = browser.find_element_by_id("input_value").text
    answer = calc(x)
    browser.find_element_by_id("answer").send_keys(answer)
    solve.click()

    result = browser.switch_to.alert.text.split(': ')[-1]
    print(result)

finally:
    time.sleep(5)
    browser.quit()
