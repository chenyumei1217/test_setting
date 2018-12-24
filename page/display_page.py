from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import base

class DisplayPage(BaseAction):

    #谁调用 我 谁给我传一个driver 当类初始化的时候这个方法就执行
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    #每个功能都定义到函数里面 功能：点击搜索按钮
    def search_click(self):
        self.click_element(base.display_page_searchId)

    #向搜索框里输入内容
    def input_src_text(self,content):
        self.input_element_content(base.display_page_src_text,content)
    #点击后退按钮
    def back_btn(self):
        self.click_element(base.display_page_back)

