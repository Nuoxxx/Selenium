#coding:utf-8
import unittest
from selenium import webdriver

class View_Activity(unittest.TestCase):
    # 测试前的初始化工作
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 隐式等待，如果在30S内页面加载完成，进行后续代码；最多等待30S，然后进行后续代码
        # 隐性等待对整个driver的周期都起作用
        self.driver.implicitly_wait(30)
        self.base_url = "http://wap.greatplus.com.cn/party/detail/2661"
        # 脚本运行时，错误的信息将被打印到这个列表中
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_something(self):
        driver = self.driver
        driver.get(self.base_url)
        time = self.driver.find_element_by_xpath("/html/body/div[3]/ul/li[1]/span[1]")
        self.assertEqual(time.text,u'时间：','xpath绝对路径')

        time2 = self.driver.find_element_by_xpath('//li[1]/span[1]')
        self.assertEqual(time.text, u'时间：', 'xpath相对路径')

        # d_time =self.driver.find_element_by_css_selector('body > div.a_simple > ul > li:nth-child(3) > span.a_dead')
        d_time =self.driver.find_element_by_css_selector('.a_dead')
        self.assertEqual(d_time.text, u'截止日期：', 'CSS')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
