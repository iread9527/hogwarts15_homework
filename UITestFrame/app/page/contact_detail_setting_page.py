# -*-coding:utf-8-*-

from UITestFrame.app.page.base_page import BasePage
from UITestFrame.app.page.contact_edit_page import ContactEditPage


class ContactDetailSettingPage(BasePage):

    def edit_member(self):
        self.parse_yaml('../resources/contact_detail_setting_page.yaml', 'edit_member')
        return ContactEditPage(self.driver)
