# -*-coding:utf-8-*-

from UITestFrame.app.page.base_page import BasePage
from UITestFrame.app.page.contact_detail_setting_page import ContactDetailSettingPage


class ContactDetailBriefInfoProfilePage(BasePage):

    def click_settings_button(self):
        self.parse_yaml('../resources/contact_detail_brief_info_page.yaml', 'click_settings_button')
        return ContactDetailSettingPage(self.driver)
