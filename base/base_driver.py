from appium import webdriver

#初始化driver对象函数
'''
调用这个方法就返回一个driver对象

'''
def init_driver():
    desired_caps = {}

    # 设备信息
    desired_caps['platformName'] = 'Android'  # 平台名称
    desired_caps['platformVersion'] = '5.1'  # 平台版本
    desired_caps['deviceName'] = '192.168.56.101:5555'  # 设备号

    # app信息
    desired_caps['appPackage'] = 'com.android.settings'  # 应用包名
    desired_caps['appActivity'] = '.Settings'  # 代表启动的activity

    # 以后模拟器支持中文输入
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 声明driver对象
