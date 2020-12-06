# -*-coding:utf-8-*-
import yaml
from appium.webdriver import webdriver
from appium.webdriver.common.mobileby import MobileBy

from WebUI.UITestFrame.page.base_page import BasePage
from WebUI.UITestFrame.page.department_search_page import DepartmentSearchPage
from WebUI.UITestFrame.page.member_invite_menu_page import MemberInviteMenuPage


class AddressBookPage(BasePage):

    def add_member(self):
        # 制造一个假弹窗, 通讯录页面，添加成员
        self.parse_yaml('../resources/address_book_page.yaml', 'add_member')
        return MemberInviteMenuPage(self.driver)

    def click_search_button(self):
        self.parse_yaml('../resources/address_book_page.yaml', 'click_search_button')
        return DepartmentSearchPage(self.driver)
