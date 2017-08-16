# coding = utf-8

import sys
import unittest
import HTMLTestRunner

import allcase_list

testsuite = unittest.TestSuite()

# testsuite.addTest(unittest.makeSuite(baidu.Baidu))
# testsuite.addTest(unittest.makeSuite(youdao.Youdao))

alltestnames = allcase_list.caselist()

for test in alltestnames:
    testsuite.addTest(unittest.makeSuite(test))

filename = 'D:\\Selenium_python\\report\\result.html'
fp = open(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description='用例执行情况')
runner.run(testsuite)