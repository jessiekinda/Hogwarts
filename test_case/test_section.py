from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_select_course():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        # self.driver.quit()
        pass

    def test_course1(self):
        self.driver.get("https://login.xueersi.com/?redirect_url=https%3A%2F%2Fwww.xueersi.com%2F")
        self.driver.find_element_by_css_selector()



