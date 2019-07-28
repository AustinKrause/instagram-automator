from selenium import webdriver
import selenium
import os
import time

class Automator:

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
        self.driver = webdriver.Chrome('chromedriver')

        self.login()

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)
        user_input = self.driver.find_element_by_name('username')
        pw_input = self.driver.find_element_by_name('password')
        
        user_input.send_keys(self.username)
        pw_input.send_keys(self.password)
        
        self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()



if __name__ == '__main__':
    ig_automator = Automator('temp_un', 'temp_pw')