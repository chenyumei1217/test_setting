
import time,os,sys
#通过sys获取系统的环境，把当前项目目录配置到环境变量中，pystest就能运行base_driver.py
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.display_page import DisplayPage
import pytest
import yaml
import allure

#读取yaml文件获取动态测试数据
def read_setting_data():
    with open("./data/setting_data.yaml","r") as f:
       file_data= yaml.load(f)
       data=file_data.get("data") #通过键获取值
       return data

class Test_Netword:
    def setup(self):
        self.driver = init_driver()
        self.display_page = DisplayPage(self.driver)

    def teardown(self):
        self.driver.close_app()  # 关闭app
        self.driver.quit()

    #点击搜索，输入aaa，点击退回
    @pytest.mark.parametrize("content",read_setting_data())
    @allure.step('测试设置页的搜索步骤')
    def test_search(self,content):
        allure.attach("描述1","点击‘显示’")
        self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        #调用点击搜索方法
        allure.attach("描述2", "点击'搜索'按钮")
        self.display_page.search_click()
        #调用输入aaa的方法
        allure.attach("描述3", "输入要搜索的内容")
        self.display_page.input_src_text(content)
        #调用点击退回按钮
        allure.attach("描述4", "点击'返回'按钮")
        self.display_page.back_btn()


