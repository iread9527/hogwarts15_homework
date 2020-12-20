# -*-coding:utf-8-*-
import yaml
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from UITestFrame.app.util.utils import handle_black_list


class BasePage:
    black_list = [(MobileBy.XPATH, '//*[@class="android.widget.TextView"]')]

    def __init__(self, driver: webdriver = None):
        self.driver = driver

    def find_by_scroll(self, text):
        return self.find(MobileBy.ANDROID_UIAUTOMATOR,
                         f'new UiScrollable(new UiSelector().scrollable(true).instance(0))\
                         .scrollIntoView(new UiSelector().text("{text}").instance(0));')

    @handle_black_list
    def find(self, by, locator=None) -> WebElement:
        # 通过黑名单装饰器处理元素定位中的弹窗
        # 使用装饰器，调用的时候就是调用装饰器函数，所以装饰器里需要return
        if locator:
            return self.driver.find_element(by, locator)
        return self.driver.find_element(*by)

    def get_toast_text(self):
        toast_text = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return toast_text

    def parse_yaml(self, path, func_name):
        with open(path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        self.parse(data[func_name])

    def wait_for_next(self, driver):
        # 适用于按钮点击无反应,需要等待下一个元素出现的情况,并没有完成
        locator = (MobileBy.CSS_SELECTOR, 'div[class="js_has_member"] a[class~="js_add_member"]')
        try:
            self.find(*locator).click()
            return self.find(MobileBy.ID, "username")
        except:
            return False

    def parse(self, steps):
        for step in steps:
            if 'click' == step['action']:
                self.find(step['by'], step['locator']).click()
            elif 'send' == step['action']:
                self.find(step['by'], step['locator']).send_keys(step['content'])
            elif 'wait_visibility' == step['action']:
                WebDriverWait(self.driver, 10).until(
                    expected_conditions.visibility_of_element_located((step['by'], step['locator'])))
            elif 'wait_clickable' == step['action']:
                WebDriverWait(self.driver, 10).until(
                    expected_conditions.element_to_be_clickable((step['by'], step['locator'])))
            elif 'custom_wait' == step['action']:
                # 适用于某个元素加载慢的情况
                WebDriverWait(self.driver, 10).until(lambda x: self.find(step['by'], step['locator']))
