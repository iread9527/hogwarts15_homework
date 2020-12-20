# -*-coding:utf-8-*-

from UITestFrame.app.page.base_page import BasePage


class ContactAddPage(BasePage):

    def add_contact(self):
        # 设置用户名,性别,手机号
        self.parse_yaml('../resources/contact_add_page.yaml', 'add_contact')
        result = self.get_toast_text()
        return result
