from appium import webdriver


# 将需要重复使用的初始化driver抽取到base_driver中
def init_driver():
    desired_caps = {
        "platformName": "android",
        "platformVersion": 8,
        "deviceName": "sherven",
        "appPackage": "com.android.messaging",
        "appActivity": ".ui.conversationlist.ConversationListActivity",
        "resetKeyboard": True,
        "unicodeKeyboard": True

    }

    return webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
