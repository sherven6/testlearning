from appium import webdriver

desired_caps = {
    "platformName": "android",
    "platVersion": 8,
    "deviceName": "sherven",
    "appPackage": "com.android.settings",
    "appActivity": ".Settings"
}


def initDriver():
    dr = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    return dr
