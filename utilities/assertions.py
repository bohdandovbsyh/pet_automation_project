import inspect
import allure

from utilities.driver_manager import DriverWrapper


class Assertions:
    def __init__(self):
        self.driver = DriverWrapper.get_driver()

    @allure.step
    def assert_with_screenshot(self, actual, expected, message):
        self.driver.save_screenshot(f".\\screenshots\\{inspect.stack()[1][3]}.png")
        assert actual == expected, message
