from selenium.webdriver.common.by import By


"""
1.搜索功能
"""
# 把find_element里面的参数给抽取出来，因为是不断变化的
display_page_searchId = (By.ID, "com.android.settings:id/search")
display_page_src_text = (By.ID, "android:id/search_src_text")
display_page_back = (By.CLASS_NAME, "android.widget.ImageButton")
"""
2.修改网络
"""
display_page_more = (By.XPATH, "//*[contains(@text,'更多')]")
display_page_mobile_network = (By.XPATH, "//*[contains(@text,'移动网络')]")
display_page_first_network = (By.XPATH, "//*[contains(@text,'首选网络')]")
display_page_network_2g = (By.XPATH, "//*[contains(@text,'2G')]")
display_page_network_3g = (By.XPATH, "//*[contains(@text,'3G')]")

