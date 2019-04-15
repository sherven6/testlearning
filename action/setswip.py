from appium.webdriver.common.touch_action import TouchAction
from base.base_driver import initDriver
import time

dr = initDriver()

dr.swipe(100, 1000, 100, 100)

dr.find_element_by_xpath('//*[contains(@text,"安全性")]').click()
time.sleep(2)

dr.find_element_by_xpath('//*[contains(@text,"屏幕锁定")]').click()
time.sleep(2)

dr.find_element_by_xpath('//*[contains(@text,"图案")]').click()

time.sleep(2)

TouchAction(dr).press(x=263, y=858).move_to(x=804, y=862).wait(200).move_to(x=265, y=1400).wait(200).move_to(x=805,
                                                                                                             y=1400).release().perform()
#
# TouchAction(dr)
