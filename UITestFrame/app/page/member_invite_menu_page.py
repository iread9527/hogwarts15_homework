# -*-coding:utf-8-*-

from UITestFrame.app.page.base_page import BasePage
from UITestFrame.app.page.contact_add_page import ContactAddPage


class MemberInviteMenuPage(BasePage):

    def add_member_by_input(self):
        # 点击手动输入添加
        self.parse_yaml('../resources/member_invite_menu_page.yaml', 'add_member_by_input')
        return ContactAddPage(self.driver)
