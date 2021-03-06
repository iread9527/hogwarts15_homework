# -*-coding:utf-8-*-

from UITestFrame.app.page.base_page import BasePage
from UITestFrame.app.page.contact_detail_brief_info_page import ContactDetailBriefInfoProfilePage


class DepartmentSearchPage(BasePage):

    def search_member(self, member_name):
        # 进入查找页面，找到成员，点击成员
        self.parse_yaml('../resources/department_search_page.yaml', 'search_member')
        return ContactDetailBriefInfoProfilePage(self.driver)
