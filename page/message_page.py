from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MessagePage(BaseAction):
    NEW_MESSAGE_BUTTON = By.ID, "com.android.messaging:id/start_new_conversation_button"
    # "com.android.messaging:id/start_new_conversation_button"
    RECEIVE_BUTTON = By.XPATH, "//*[@text='收件人']"
    OK = By.XPATH, "//*[@text='常用联系人']"
    INPUT_TEXT = By.ID, "com.android.messaging:id/compose_message_text"
    SEND_BUTTON = By.ID, "com.android.messaging:id/self_send_icon"

    # def __init__(self, driver):
    #     BaseAction().__init__(self, driver)

    def click_new_message(self):
        self.click(self.NEW_MESSAGE_BUTTON)

    def input_receive(self, value):
        self.input_text(self.RECEIVE_BUTTON, value)

    def select_receive(self):
        self.click(self.OK)

    def input_message(self, value):
        self.input_text(self.INPUT_TEXT, value)

    def send_message(self):
        self.click(self.SEND_BUTTON)
