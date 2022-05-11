import configparser
import os

abs_path = os.path.abspath(r"..\..\configurations\run_settings.ini")
config = configparser.RawConfigParser()
config.read(abs_path)


class ReadConfig:
    @staticmethod
    def get_application_url():
        return config.get('app_info', 'base_url')

    @staticmethod
    def get_user_email():
        return config.get('app_info', 'user_name')

    @staticmethod
    def get_password():
        return config.get('app_info', 'password')

    @staticmethod
    def get_browser():
        return config.get('browser', 'browser_id')

    @staticmethod
    def get_logging_level():
        return config.get('logging_level', 'logging_level')

    @staticmethod
    def get_api_base_url():
        return config.get('api_data', 'base_url')
