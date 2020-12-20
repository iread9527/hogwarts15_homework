# -*-coding:utf-8-*-

from UITestFrame.app.util import utils
from UITestFrame.web.page.web import Web


class TestAddMembers:

    def setup(self):
        self.we_work_web = Web()
        self.main_page = self.we_work_web.start().goto_main_page()

    def teardown(self):
        self.we_work_web.stop()

    def test_add_members(self):
        user_name = 'user' + utils.time_stamp()
        account_id = 'account' + utils.time_stamp()
        phone_num = utils.random_phone()
        self.main_page.goto_contacts_page().add_members(user_name=user_name, account_id=account_id, phone_num=phone_num)
