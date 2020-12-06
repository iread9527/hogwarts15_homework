# -*-coding:utf-8-*-
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote import webdriver

from WebUI.UITestFrame.page.base_page import BasePage
from WebUI.UITestFrame.page.contact_detail_setting_page import ContactDetailSettingPage


class ContactDetailBriefInfoProfilePage(BasePage):

    def click_settings_button(self):
        self.parse_yaml('../resources/contact_detail_brief_info_page.yaml', 'click_settings_button')
        return ContactDetailSettingPage(self.driver)
