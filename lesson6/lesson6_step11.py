from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    # link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector(".first[required]")
    first_name.send_keys("Ricardo")
    last_name = browser.find_element_by_css_selector(".second[required]")
    last_name.send_keys("Milos")
    email = browser.find_element_by_css_selector(".third[required]")
    email.send_keys("megaman@best.com")
    
    # Заполняем необязательные поля
    phone = browser.find_element_by_css_selector(".second_block .first")
    phone.send_keys("88005553535")
    address = browser.find_element_by_css_selector(".second_block .second")
    address.send_keys("Heaven")

    # Отправляем заполненную форму
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

