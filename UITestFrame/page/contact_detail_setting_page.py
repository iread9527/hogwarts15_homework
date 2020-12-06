# -*-coding:utf-8-*-
from appium.webdriver.common.mobileby import MobileBy

from WebUI.UITestFrame.page.base_page import BasePage
from WebUI.UITestFrame.page.contact_edit_page import ContactEditPage


class ContactDetailSettingPage(BasePage):

    def edit_member(self):
        self.parse_yaml('../resources/contact_detail_setting_page.yaml', 'edit_member')
        return ContactEditPage(self.driver)
