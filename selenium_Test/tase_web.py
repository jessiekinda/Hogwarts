import shelve

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
#显示等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestDemo():
    def setup(self):
        self.driver=webdriver.Chrome()

        # options=Options()
        # options.debugger_address="127.0.0.1:9222"
        # self.driver=webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def teardown(self):
        pass
        #self.driver.quit()

    def test_update_cookies_to_db(self):
        # 1. 连接数据库
        db = shelve.open("db/cookies")
        # 2. 打开登录网页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        # 3. 给扫码动作预留 5s
        sleep(5)
        # 4. 扫码成功，获取cookies
        cookies = self.driver.get_cookies()
        # 5. cookies存储到db
        db['cookie'] = cookies
        # 6. 用完数据库关闭
        db.close()

    def test_cookies(self):
        # 1. 连接数据库
        db = shelve.open("db/cookies")
        # 2. 从数据库读取cookies
        cookies=db['cookie']
        # 3. 数据库关闭
        db.close()
        # 4. 把cookie添加到driver中
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        sleep(2)

    def test_case1(self):
        member_add = "李九"
        member_add_id = "2011007"
        member_add_phonenum = "13100002307"
        # 1. 利用cookies登录到企业微信 通讯录 页面
        self.test_cookies()
        # 2. 元素定位操作
        self.driver.find_element(By.LINK_TEXT,"通讯录").click()
        w1=WebDriverWait(self.driver,15)
        #c1=EC.title_contains("南科")
        c1=EC.presence_of_element_located((By.LINK_TEXT,"通讯录"))
        w1.until(c1)
        # 3. 添加成员
        self.driver.find_element(By.LINK_TEXT,"添加成员").click()
        self.driver.find_element(By.ID,"username").send_keys(member_add)
        self.driver.find_element(By.ID,"memberAdd_english_name").send_keys("002")
        self.driver.find_element(By.ID,"memberAdd_acctid").send_keys(member_add_id)
        # self.driver.find_element(By.LINK_TEXT,"男").click()
        self.driver.find_element(By.ID,"memberAdd_phone").send_keys(member_add_phonenum)
        self.driver.find_element(By.ID, "memberEdit_address").send_keys("龙华区")
        self.driver.find_element_by_link_text("保存并继续添加").click()
        sleep(2)
        # 4. 再次点击通讯录
        self.driver.find_element(By.LINK_TEXT, "通讯录").click()
        # 5. 断言通讯录是否存在已经添加的成员
        # 如果存在李四，则不用添加
        sleep(2)
        # 此处需要显示等待
        member_find = self.driver.find_element(By.XPATH, "//*[@id='member_list']//span").text
        # assert member_add == member_find;
        #
        assert member_add ==member_find

        # t1=self.driver.title
        # b1=t1.startswith("系统提示")
        # print(type(b1))
        # assert True(b1)
        #
        # p1=self.driver.page_source
        # assert "登录成功" in(p1)









