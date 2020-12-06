# -*-coding:utf-8-*-
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from WebUI.UITestFrame.page.base_page import BasePage


class ContactAddPage(BasePage):

    def add_contact(self):
        # 设置用户名,性别,手机号
        self.parse_yaml('../resources/contact_add_page.yaml', 'add_contact')
        result = self.get_toast_text()
        return result
