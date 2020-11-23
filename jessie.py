import selenium
from selenium import webdriver
from time import sleep

class TestTmooc():
    def setup(self):
        self.drive = webdriver.Chrome()
        self.drive.maximize_window()
        self.drive.implicitly_wait(5)

    def teardown(self):
        self.drive.quit()
    def testtmooc(self):
        self.drive.get("http://www.tmooc.cn/")
        sleep(3)
        self.drive.find_element_by_link_text("登录").click()
        print(self.drive.current_window_handle)
        self.drive.find_element_by_link_text("线上班").click()
        print(self.drive.current_window_handle)
        print(self.drive.window_handles)
        windows= self.drive.window_handles
        self.drive.find_element_by_link_text("进入教室").click()


        self.drive.find_element_by_id()