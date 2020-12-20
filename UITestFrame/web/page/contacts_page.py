# -*-coding:utf-8-*-

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from UITestFrame.app.page.base_page import BasePage


class ContactsPage(BasePage):

    def add_members(self, user_name, account_id, phone_num):

        locator = (MobileBy.CSS_SELECTOR, 'div[class="js_has_member"] a[class~="js_add_member"]')

        def wait_for_next(driver: WebDriver):
            # 适用于按钮点击无反应的情况
            try:
                driver.find_element(*locator).click()
                return driver.find_element(MobileBy.ID, "username")
            except StaleElementReferenceException:
                return False

        WebDriverWait(self.driver, 10).until(wait_for_next)
        self.find(MobileBy.CSS_SELECTOR, '#username').send_keys(user_name)
        self.find(MobileBy.CSS_SELECTOR, '#memberAdd_acctid').send_keys(account_id)
        self.find(MobileBy.CSS_SELECTOR, '#memberAdd_phone').send_keys(phone_num)
        self.find(MobileBy.CSS_SELECTOR, '.js_btn_save').click()
        # 使用搜索功能校验创建的用户名
        self.find(MobileBy.CSS_SELECTOR, '#memberSearchInput').send_keys(user_name)
        created_user_name = self.find(MobileBy.CSS_SELECTOR, '.ww_searchResult_title_peopleName').text
        assert created_user_name == user_name
