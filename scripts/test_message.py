import yaml, sys, os
import allure

sys.path.append(os.getcwd())
from appium import webdriver
import pytest

from base.base_driver import init_driver
from page.message_page import MessagePage


def data_with_key(key):
    with open("./data" + key + ".yml", 'r') as f:
        return yaml.load(f)


class TestMessage:
    def setup(self):
        self.dr = init_driver()
        self.message_page = MessagePage(self.dr)

    # @pytest.mark.parametrize("value",[10086,"你好世界"])
    def test_send_message(self):
        self.message_page.click_new_message()

        self.message_page.input_receive("10086")

        self.message_page.select_receive()

        self.message_page.input_message("nihao , world")

        self.message_page.send_message()
