import threading

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.utils import ChromeType
"""
CLASS FOR MANAGING WEB_DRIVER
"""


class DriverWrapper:
    CHROME = 1
    FIRE_FOX = 2
    CHROMIUM = 3

    __DRIVER_MAP = {}

    @staticmethod
    def create_driver(driver_id):
        """
        Create driver func
        :param driver_id: int, get driver id from this class
        :return: WebDriver instance
        """
        thread_obj = threading.currentThread()

        def get_driver():
            if DriverWrapper.CHROME == driver_id:
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            elif DriverWrapper.FIRE_FOX == driver_id:
                driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
            elif DriverWrapper.CHROMIUM == driver_id:
                driver = webdriver.Chrome(
                    service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
            else:
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            return driver

        DriverWrapper.__map(thread_obj, get_driver())
        return DriverWrapper.get_driver()

    @staticmethod
    def get_driver():
        """
        @description: Get web_driver for current thread
        :return: WebDriver for current thread
        """
        return DriverWrapper.__DRIVER_MAP[threading.current_thread()]["driver"]

    @staticmethod
    def shutdown():
        """
        @description: shutdown web driver
        """
        DriverWrapper.get_driver().quit()

    @staticmethod
    def __map(thread, driver):
        """
        @description: add driver to driver map
        :param thread: current thred
        :param driver: thread driver
        """
        DriverWrapper.__DRIVER_MAP[thread] = {"driver": driver}

    @staticmethod
    def get_driver_map():
        """
        :return: DriverMap
        """
        return DriverWrapper.__DRIVER_MAP

    @staticmethod
    def back():
        DriverWrapper.get_driver().back()
