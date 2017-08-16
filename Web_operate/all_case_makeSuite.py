# coding = utf-8

import sys,os
import unittest
import HTMLTestRunner

sys.path.append("\Selenium_Learn")
from Selenium_Learn.Web_operate.ceses import start_baidu
from Selenium_Learn.Web_operate.ceses import youdao

testsuite = unittest.TestSuite()
# 通过unittest.makeSuite添加待执行用例
testsuite.addTest(unittest.makeSuite(start_baidu.Baidu))
testsuite.addTest(unittest.makeSuite(youdao.Youdao))


filename = os.path.abspath(os.path.join(os.path.abspath(__file__),"../report/result.html"))
fp = open(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况')
runner.run(testsuite)