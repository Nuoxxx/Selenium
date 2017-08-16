# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, re
import HTMLTestRunner


class Baidu(unittest.TestCase):
    # 测试前的初始化工作
    def setUp(self):
        self.driver = webdriver.Firefox()
        # 隐式等待，如果在30S内页面加载完成，进行后续代码；最多等待30S，然后进行后续代码
        # 隐性等待对整个driver的周期都起作用
        self.driver.implicitly_wait(30)
        self.base_url = "http:www.youdao.com/"
        # 脚本运行时，错误的信息将被打印到这个列表中
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_youdao_search(self):
        u"""搜索Selenium"""
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("query").send_keys(u"虫师")
        driver.find_element_by_id("qb").click()
        time.sleep(2)
        # driver.close()


    # 测试后的清除工作，比如资源的释放
    def tearDown(self):
        self.driver.quit()
        # 对前面verificationErrors方法获得的列表进行比较；如查verificationErrors的列表不为空输出列表中的报错信息
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()


