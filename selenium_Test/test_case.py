import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_web():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_horgworts(self):
        # self.driver.get("https://ceshiren.com/")
        # self.driver.find_element_by_link_text("热门").click()
        # # self.driver.find_element_by_link_text("#ember605 .title").click()
        # self.driver.find_element_by_css_selector("#ember290 > td.main-link.clearfix > span > a").click()
        # # self.driver.find_element_by_xpath("//a[contains(text(),'【15期测试开发】【直播】python pytest测试实战 1')]").click()
        self.driver.get('http://www.baidu.com')
        #self.driver.find_element_by_id(id_='kw').send_keys('霍格沃茨测试学院')
        #self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys("霍格沃茨测试学院")
        self.driver.find_element(By.CSS_SELECTOR,'[id=kw]').send_keys("霍格沃茨测试学院")
        self.driver.find_element(By.ID,'su').click()
        #self.driver.find_element_by_id(id_='su').click()


