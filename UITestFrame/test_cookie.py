# -*-coding:utf-8-*-
import shelve
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestCookie:
    def setup(self):
        # 复用浏览器
        # options = Options()
        # options.debugger_address = 'localhost:9222'
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # time.sleep(10)

    def teardown(self):
        self.driver.quit()

    def test_save_cookie(self):
        # 这一步不要关闭浏览器，不然cookie失效
        cookies = self.driver.get_cookies()
        db = shelve.open('cookies')
        db['cookie'] = cookies
        db.close()

    def test_index_page(self):
        db = shelve.open('cookies')
        cookies = db['cookie']
        db.close()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_uploadInputMask').send_keys(
            '/home/manx/Desktop/wode.xlsx')
        file_name = self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_fileNames').text
        assert file_name == 'wode.xlsx'
