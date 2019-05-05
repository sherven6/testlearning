from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.dr = driver

    # 点击按钮
    def click(self, loc):
        self.find_element(loc).click()

    # 想输入框输入文字
    def input_text(self, loc, value):
        self.find_element(loc).send_keys(value)

    # 封装find元素操作,加入了显式等待
    def find_element(self, loc):
        return WebDriverWait(self.dr, 30, 1).until(lambda x: x.find_element(loc[0], loc[1]))
