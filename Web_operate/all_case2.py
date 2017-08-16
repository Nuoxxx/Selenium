# coding = utf-8
# 通过defaultTestLoader加载以特定命名规则的.py文件
import sys,time,os
import unittest
import HTMLTestRunner

filenameaa = os.path.abspath(os.path.join(os.path.abspath(__file__),'../ceses'))
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
filename = os.path.abspath(os.path.join(os.path.abspath(__file__),'../report/'+now+"result.html"))
fp = open(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description='用例执行情况')
runner.run(alltestnames)