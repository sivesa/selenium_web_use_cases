from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.NAME, 'email')  # Adjust selector as needed
        self.password_input = (By.NAME, 'password')  # Adjust selector as needed
        self.sign_in_button = (By.NAME, 'submit')  # Adjust selector as needed

    def enter_email(self, email):
        email_element = self.driver.find_element(*self.email_input)
        email_element.click()
        email_element.send_keys(email)

    def enter_password(self, password):
        password_element = self.driver.find_element(*self.password_input)
        password_element.click()
        password_element.send_keys(password)

    def click_sign_in(self):
        sign_in_element = self.driver.find_element(*self.sign_in_button)
        sign_in_element.click()


class TestLogin:
    def __init__(self):
        self.driver = webdriver.Firefox()  # Ensure chromedriver is in your PATH or provide the path to it
        self.driver.get('http://127.0.0.1:8000/login.php')  # Replace with the actual URL

    def perform_login(self, email, password):
        login_page = LoginPage(self.driver)
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_sign_in()

    def close_browser(self):
        time.sleep(5)  # Optional: Pause to observe the result (not recommended for production code)
        self.driver.quit()

def read_credentials(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['email'], data['password']

if __name__ == "__main__":
    email, password = read_credentials('config.json')
    test = TestLogin()
    test.perform_login(email, password)
    test.close_browser()
