# coding = utf-8

import sys,time
import unittest
import HTMLTestRunner

filenameaa = 'D:\Selenium_python\ceses'
def createsuitell():
    testsuite = unittest.TestSuite()

    discover = unittest.defaultTestLoader.discover(filenameaa,pattern='start_*.py')

    for test_suite in discover:
        for test_case in test_suite:
            testsuite.addTests(test_case)
            print(testsuite)
    return testsuite

alltestnames = createsuitell()

now = time.strftime('%Y-%m-%M_%H_%M_%S',time.localtime(time.time()))
filename = 'D:\\Selenium_python\\report\\'+now+'result.html'
fp = open(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description='用例执行情况')
runner.run(alltestnames)