# -*-coding:utf-8-*-
import functools
import os
import time

import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def handle_black_list(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        from WebUI.UITestFrame.page.base_page import BasePage
        # 类里面的方法装饰器，args[0]就是实例本身
        instance: BasePage = args[0]
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            # 对黑名单里面弹窗元素进行定位关闭，关闭后重新查找，如果循环结束都没有黑名单，抛出异常
            screenshot_name = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()) + '.png'
            screenshot_path = os.path.join('../screenshot/', screenshot_name)
            instance.driver.save_screenshot(screenshot_path)
            with open(screenshot_path, 'rb') as f:
                content = f.read()
            allure.attach(content, attachment_type=allure.attachment_type.PNG)
            for ele_locator in instance.black_list:
                ele = instance.driver.find_elements(*ele_locator)
                if ele:
                    WebDriverWait(instance.driver, 10).until(expected_conditions.element_to_be_clickable(ele_locator))
                    ele[0].click()
                    return func(*args, **kwargs)
            raise e

    return wrapper
