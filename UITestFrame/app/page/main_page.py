# -*-coding:utf-8-*-

from UITestFrame.app.page.address_book_page import AddressBookPage
from UITestFrame.app.page.base_page import BasePage


class MainPage(BasePage):

    def goto_address_book_page(self):
        # 点击进入通讯录页面
        self.parse_yaml('../resources/main_page.yaml', 'goto_address_book_page')
        return AddressBookPage(self.driver)
