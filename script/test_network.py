import time,os,sys
#通过sys获取系统的环境，把当前项目目录配置到环境变量中，pystest就能运行base_driver.py
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.network_page import NetworkPage

class Test_Netword:
    def setup(self):
        self.driver = init_driver()
        self.network_page=NetworkPage(self.driver)
    def teardown(self):
        self.driver.close_app()  # 关闭app
        self.driver.quit()

    def test_2G(self):
        self.network_page.click_more()
        self.network_page.click_mobile_network()
        self.network_page.click_first_network()
        self.network_page.click_net_2g()

    def test_3G(self):
        self.network_page.click_more()
        self.network_page.click_mobile_network()
        self.network_page.click_first_network()
        self.network_page.click_net_3g()