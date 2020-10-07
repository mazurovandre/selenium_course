from selenium import webdriver
import math, time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  browser = webdriver.Chrome()
  link = "https://SunInJuly.github.io/execute_script.html"
  browser.get(link)

  value = browser.find_element_by_id('input_value').text
  answer = calc(value)

  input = browser.find_element_by_id('answer')
  input.send_keys(answer)
  checkbox = browser.find_element_by_id('robotCheckbox')
  radio = browser.find_element_by_id('robotsRule')
  button = browser.find_element_by_tag_name("button")
  browser.execute_script("return arguments[0].scrollIntoView(true);", button)
  checkbox.click()
  radio.click()
  button.click()
finally:
  time.sleep(10)
  browser.quit()
