# -*-coding:utf-8-*-
from appium import webdriver

from UITestFrame.app.page.base_page import BasePage
from UITestFrame.app.page.main_page import MainPage


class App(BasePage):

    def start(self):
        if self.driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '10'
            desired_caps['deviceName'] = 'my_device'
            # 已经启动的应用继续进行操作，每次都要返回初始页面
            # desired_caps['dontStopAppOnReset'] = True
            desired_caps['noReset'] = True
            desired_caps['skipDeviceInitialization'] = True
            desired_caps['skipServerInstallation'] = True
            # 保持会话10分钟便于调试
            desired_caps['newCommandTimeout'] = 600
            # 雪球app
            # desired_caps['appPackage'] = 'com.xueqiu.android'
            # desired_caps['appActivity'] = '.main.view.MainActivity'
            # 企业微信app
            desired_caps['appPackage'] = 'com.tencent.wework'
            desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        # 这里很细节，返回对象自身，就可以链式调用
        return self

    def stop(self):
        self.driver.quit()

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def goto_main_page(self):
        return MainPage(self.driver)
