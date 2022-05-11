import threading

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.utils import ChromeType

from utilities.read_run_settings import ReadConfig


class DriverWrapper:
    CHROME = 1
    FIRE_FOX = 2
    CHROMIUM = 3

    __DRIVER_MAP = {}

    @staticmethod
    def create_driver(driver_id):
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
        return DriverWrapper.__DRIVER_MAP[threading.current_thread()]["driver"]

    @staticmethod
    def shutdown():
        DriverWrapper.get_driver().quit()

    @staticmethod
    def __map(thread, driver):
        DriverWrapper.__DRIVER_MAP[thread] = {"driver": driver}

    @staticmethod
    def get_driver_map():
        return DriverWrapper.__DRIVER_MAP

    @staticmethod
    def back():
        DriverWrapper.get_driver().back()
