# -*-coding:utf-8-*-
from appium.webdriver.common.mobileby import MobileBy
from UITestFrame.app.page.base_page import BasePage
from UITestFrame.web.page.contacts_page import ContactsPage


class MainPage(BasePage):

    def goto_contacts_page(self):
        self.find(MobileBy.CSS_SELECTOR, '#menu_contacts').click()
        return ContactsPage(self.driver)
