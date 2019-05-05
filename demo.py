import time

from appium import webdriver

desired_caps = {
    "platformName": "android",
    "platformVersion": 8,
    "deviceName": "sherven",
    "appPackage": "com.android.messaging",
    "appActivity": ".ui.conversationlist.ConversationListActivity",
    "resetKeyboard": True,
    "unicodeKeyboard": True

}

dr = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

dr.find_element_by_id("com.android.messaging:id/start_new_conversation_button").click()
time.sleep(3)
dr.find_element_by_xpath("//*[@text='收件人']").send_keys("10086")
time.sleep(3)
dr.find_element_by_xpath("//*[@text='常用联系人']").click()
time.sleep(3)
dr.find_element_by_id("com.android.messaging:id/compose_message_text").send_keys("nihao，世界")
time.sleep(3)
dr.find_element_by_id("com.android.messaging:id/self_send_icon").click()
time.sleep(8)
dr.close_app()
