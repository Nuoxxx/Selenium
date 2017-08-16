# coding = utf-8

import sys,os
import unittest
import HTMLTestRunner

sys.path.append("\Selenium_Learn")
from  Selenium_Learn.Web_operate import allcase_list
testsuite = unittest.TestSuite()
#借助allcase_list添加用例
alltestnames = allcase_list.caselist()

for test in alltestnames:
    testsuite.addTest(unittest.makeSuite(test))


filename = os.path.abspath(os.path.join(os.path.abspath(__file__),"../report/result.html"))
fp = open(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description='用例执行情况')
runner.run(testsuite)