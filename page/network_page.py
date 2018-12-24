from selenium.webdriver.common.by import By
import base
from base.base_action import BaseAction
class NetworkPage(BaseAction):

    def __init__(self,driver):
        BaseAction.__init__(self,driver)
    def click_more(self):
        self.click_element(base.display_page_more)

    def click_mobile_network(self):
        self.click_element(base.display_page_mobile_network)

    def click_first_network(self):
        self.click_element(base.display_page_first_network)

    def click_net_2g(self):
        self.click_element(base.display_page_network_2g)

    def click_net_3g(self):
        self.click_element(base.display_page_network_3g)