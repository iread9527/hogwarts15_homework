# -*-coding:utf-8-*-
import shelve
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestCookie:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        time.sleep(15)

    def test_save_cookie(self):
        # 这一步不要关闭浏览器，不然cookie失效
        cookies = self.driver.get_cookies()
        db = shelve.open('cookies')
        db['cookie'] = cookies
        db.close()
