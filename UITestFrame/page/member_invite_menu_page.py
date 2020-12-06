# -*-coding:utf-8-*-
from appium.webdriver.common.mobileby import MobileBy

from WebUI.UITestFrame.page.base_page import BasePage
from WebUI.UITestFrame.page.contact_add_page import ContactAddPage


class MemberInviteMenuPage(BasePage):

    def add_member_by_input(self):
        # 点击手动输入添加
        self.parse_yaml('../resources/member_invite_menu_page.yaml', 'add_member_by_input')
        return ContactAddPage(self.driver)
