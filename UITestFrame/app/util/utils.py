# -*-coding:utf-8-*-
import functools
import os
import random
import time

import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def handle_black_list(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        from UITestFrame.app.page.base_page import BasePage
        # 类里面的方法装饰器，args[0]就是实例本身
        instance: BasePage = args[0]
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            # 对黑名单里面弹窗元素进行定位关闭，关闭后重新查找，如果循环结束都没有黑名单，抛出异常
            screenshot_name = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()) + '.png'
            screenshot_path = os.path.join('../screenshot', screenshot_name)
            print(screenshot_path)
            instance.driver.save_screenshot(screenshot_path)
            print(instance)
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


def time_stamp():
    time_now = time.strftime('%Y%m%d%H%M%S', time.localtime())
    return str(time_now)


def random_phone():
    pre_list = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                "186", "187", "188", "189"]
    phone_num = random.choice(pre_list) + "".join(random.choice("0123456789") for i in range(8))
    return str(phone_num)


def base_dir():
    return os.path.dirname(os.path.dirname(__file__))


if __name__ == '__main__':
    print(base_dir())
