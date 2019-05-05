from appium import webdriver
import allure

desired_caps = {}
desired_caps['platformName'] = "Android"
desired_caps['platformVersion'] = "8.0.0"
desired_caps['deviceName'] = "Google Pixel"
desired_caps["appPackage"] = "com.android.messaging"
desired_caps['appActivity'] = ".ui.conversationlist.ConversationListActivity"

dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

dr.find_element_by_id("com.android.messaging:id/start_new_conversation_button").click()
#
# # 四个参数分别代表开始的x坐标，开始的y坐标，结束的x坐标，结束的y坐标
# dr.swipe(200, 2000, 200, 200)

# class Sadasd:
#     def asd(self):
#         print('你好')
#
#
# print(123)
#
# if __name__ == '__main__':
#     a = Sadasd()
#     print('asdasda')
#     b = 1
#
#     print(type(Sadasd))
#     print(type(b))
