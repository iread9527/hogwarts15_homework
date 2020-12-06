# -*-coding:utf-8-*-
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from WebUI.UITestFrame.page.address_book_page import AddressBookPage
from WebUI.UITestFrame.page.base_page import BasePage


class MainPage(BasePage):

    def goto_address_book_page(self):
        # 点击进入通讯录页面
        self.parse_yaml('../resources/main_page.yaml', 'goto_address_book_page')
        return AddressBookPage(self.driver)
