# -*-coding:utf-8-*-

from UITestFrame.app.page.app import App


class TestWeWork:
    def setup(self):
        self.we_work_app = App()
        self.main_page = self.we_work_app.start().goto_main_page()

    def teardown(self):
        self.we_work_app.stop()

    # @pytest.mark.skip
    def test_add_contact(self):
        result = self.main_page.goto_address_book_page() \
            .add_member().add_member_by_input().add_contact()
        assert '添加成功' == result

    # @pytest.mark.skip
    def test_del_contact(self):
        # 对于发生的异常需要截图，使用数据驱动的方式写用例
        result = self.main_page.goto_address_book_page().click_search_button() \
            .search_member('aaraaa').click_settings_button().edit_member().del_member()
        assert '无搜索结果' == result
