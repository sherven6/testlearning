from appium import webdriver

desired_caps = {
    "platformName": "android",
    "platVersion": 8,
    "deviceName": "sherven",
    "automationName": "UIautomator2",
    "appPackage": "com.android.settings",
    "appActivity": ".Settings"
}


def initDriver():
    return webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
