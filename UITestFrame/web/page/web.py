# -*-coding:utf-8-*-
import shelve

from selenium import webdriver

from UITestFrame.app.page.base_page import BasePage
from UITestFrame.web.page.main_page import MainPage


class Web(BasePage):

    def start(self):
        if self.driver is None:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
            self.driver.implicitly_wait(5)
        else:
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # 这里很细节，返回对象自身，就可以链式调用
        return self

    def stop(self):
        self.driver.quit()

    def goto_main_page(self):
        db = shelve.open('../cookies')
        cookies = db['cookie']
        db.close()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        return MainPage(self.driver)
