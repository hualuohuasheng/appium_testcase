# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from xinyuan.app.appelement.base import BasePage


class 首页(BasePage):

    def 首页按钮(self):
        if self.is_android:
            return self.driver.find_element_by_id("com.ex55.app:id/activity_main_iv_main")
        else:
            return self.driver.find_element_by_id("首页")

    # (//XCUIElementTypeTable[@name="空列表"])[1]/XCUIElementTypeOther[4]/XCUIElementTypeOther[1]
    def 广场按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llSocialNewsFeed"] if self.is_android else [By.ID, '广场']
        return self.driver.find_element(ele[0], ele[1])

    # (//XCUIElementTypeTable[@name="空列表"])[1]/XCUIElementTypeOther[4]/XCUIElementTypeOther[2]
    def 群组按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llSocialGroups"] if self.is_android else [By.ID, '群组']
        return self.driver.find_element(ele[0], ele[1])

    def 好友按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llSocialChannels"] if self.is_android else [By.ID, '好友']
        return self.driver.find_element(ele[0], ele[1])

    def 首页_法币交易(self):
        ele = [By.ID, f"{self.id_loc_base}/rlTradeOTC"] if self.is_android else [By.ID, '法币交易']
        return self.driver.find_element(ele[0], ele[1])

    def 首页_公告中心(self):
        ele = [By.ID, f"{self.id_loc_base}/rlAnnouncementCenter"] if self.is_android else [By.ID, '公告中心']
        return self.driver.find_element(ele[0], ele[1])

    def 首页_帮助中心(self):
        ele = [By.ID, f"{self.id_loc_base}/rlHelpCenter"] if self.is_android else [By.ID, '帮助中心']
        return self.driver.find_element(ele[0], ele[1])

    def 首页_h5网页关闭按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/custom_header_iv_close"] if self.is_android else [By.ID, '关闭']
        return self.driver.find_element(ele[0], ele[1])

    def 首页_标题(self, iosname=None):
        ele = [By.ID, f"{self.id_loc_base}/custom_header_tv_title"] if self.is_android \
            else [By.XPATH, f"//XCUIElementTypeOther[@name='{iosname}']"]
        return self.driver.find_element(ele[0], ele[1])

    # //XCUIElementTypeApplication[@name="55.com"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/
    # XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/
    # XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTable[3]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[2]
    def 首页_币种最新价(self):
        self.driver
        ele = [By.ID, f"{self.id_loc_base}/tvMarketsMainPrice"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    # //XCUIElementTypeApplication[@name="55.com"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/
    # XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/
    # XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTable[3]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[3]
    def 首页_币种涨跌幅(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMarketsMainChange"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    # //XCUIElementTypeApplication[@name="55.com"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/
    # XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/
    # XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTable[3]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]
    def 首页_币种名称(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMarketsMainTopLeft"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    # //XCUIElementTypeApplication[@name="55.com"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/
    # XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/
    # XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeTable[2]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]
    def 首页_币种计价方式(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMarketsMainTopRight"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 首页_外汇币种名称(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMarketsMainBottom"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 首页_更多按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llMainMarketsMore"] if self.is_android else [By.ID, '更多']
        return self.driver.find_element(ele[0], ele[1])

    def 首页_滚动公告(self):
        ele = [By.ID, f"{self.id_loc_base}/llAdvertising"] if self.is_android \
            else [By.XPATH, '(//XCUIElementTypeTable[@name="空列表"])[1]/XCUIElementTypeOther[2]']
        return self.driver.find_element(ele[0], ele[1])

    # Left，Mid，Right
    def 首页_左边币种名称(self):
        ele = [By.ID, f"{self.id_loc_base}/tvLeftSymbolName"] if self.is_android \
            else [By.XPATH, "//XCUIElementTypeTable[@name='空列表']/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/"
                            "XCUIElementTypeStaticText[1]"]
        return self.driver.find_element(ele[0], ele[1])

    def 首页_左边币种价格(self):
        ele = [By.ID, f"{self.id_loc_base}/tvLeftSymbolPrice"] if self.is_android \
            else [By.XPATH, "//XCUIElementTypeTable[@name='空列表']/XCUIElementTypeScrollView/XCUIElementTypeOther[1]"
                            "/XCUIElementTypeStaticText[2]"]
        return self.driver.find_element(ele[0], ele[1])

    def 首页_左边币种涨跌幅(self):
        ele = [By.ID, f"{self.id_loc_base}/tvLeftSymbolPercent"] if self.is_android \
            else [By.XPATH, "//XCUIElementTypeTable[@name='空列表']/XCUIElementTypeScrollView/XCUIElementTypeOther[1]"
                            "/XCUIElementTypeStaticText[3]"]
        return self.driver.find_element(ele[0], ele[1])

    def 首页_左边币种换算价格(self):
        ele = [By.ID, f"{self.id_loc_base}/tvLeftSymbolCurrency"] if self.is_android \
            else [By.XPATH, "//XCUIElementTypeTable[@name='空列表']/XCUIElementTypeScrollView/XCUIElementTypeOther[1]"
                            "/XCUIElementTypeStaticText[4]"]
        return self.driver.find_element(ele[0], ele[1])
