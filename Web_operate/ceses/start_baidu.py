# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import HTMLTestRunner

class Baidu(unittest.TestCase):
    #测试前的初始化工作
    def setUp(self):
        self.driver = webdriver.Chrome()
        #隐式等待，如果在30S内页面加载完成，进行后续代码；最多等待30S，然后进行后续代码
        #隐性等待对整个driver的周期都起作用
        self.driver.implicitly_wait(30)
        self.base_url = "http:www.baidu.com/"
        #脚本运行时，错误的信息将被打印到这个列表中
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_baidu(self):
        u"""搜索Selenium"""
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("Selenium")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        # driver.close()

    def test_news(self):
        u"""点击新闻"""
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_name("tj_trnews").click()
        time.sleep(2)
        # driver.close()

    #测试后的清除工作，比如资源的释放
    def tearDown(self):
        self.driver.quit()
        #对前面verificationErrors方法获得的列表进行比较；如查verificationErrors的列表不为空输出列表中的报错信息
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
    # suite = unittest.TestSuite()
    #
    # suite.addTest(Baidu("test_baidu"))
    # suite.addTest(Baidu("test_news"))
    #
    # #获取当前时间
    # now = time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))
    # #把当前时间加到报告中
    # filename = 'D:\\Selenium_python\\test_case\\'+now+'result.html'
    # fp = open(filename,'wb')
    #
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'百度测试',description=u'用例执行')
    #
    # runner.run(suite)

