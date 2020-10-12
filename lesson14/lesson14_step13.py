from selenium import webdriver
import time
import unittest

class TestRegistration(unittest.TestCase):
    def test_reg1(self):
        try: 
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            first_name = browser.find_element_by_css_selector(".first[required]")
            first_name.send_keys("Ricardo")
            last_name = browser.find_element_by_css_selector(".second[required]")
            last_name.send_keys("Milos")
            email = browser.find_element_by_css_selector(".third[required]")
            email.send_keys("megaman@best.com")

            # Отправляем заполненную форму
            button = browser.find_element_by_xpath("//button[text()='Submit']")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text

        finally:
            browser.quit()
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Test is bad!")

    def test_reg2(self):
        try: 
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            first_name = browser.find_element_by_css_selector(".first[required]")
            first_name.send_keys("Ricardo")
            last_name = browser.find_element_by_css_selector(".second[required]")
            last_name.send_keys("Milos")
            email = browser.find_element_by_css_selector(".third[required]")
            email.send_keys("megaman@best.com")

            # Отправляем заполненную форму
            button = browser.find_element_by_xpath("//button[text()='Submit']")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text

        finally:
            browser.quit()
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Test is bad!")
        
        
if __name__ == "__main__":
    unittest.main()