# -*-coding:utf-8-*-
from time import sleep

from appium.webdriver import webdriver
from appium.webdriver.common.mobileby import MobileBy

from WebUI.UITestFrame.page.base_page import BasePage


class ContactEditPage(BasePage):
    del_member_result_locator = (MobileBy.XPATH, '//*[@text="无搜索结果"]')

    def del_member(self):
        self.parse_yaml('../resources/contact_edit_page.yaml', 'del_member')
        result = self.find(self.del_member_result_locator).get_attribute('text')
        return result
