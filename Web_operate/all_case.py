# coding = utf-8

import sys,os
import unittest
import HTMLTestRunner

sys.path.append("\selenum")

testsuite = unittest.TestSuite()

testsuite.addTest(unittest.makeSuite(start_baidu.Baidu))
testsuite.addTest(unittest.makeSuite(youdao.Youdao))

# alltestnames = allcase_list.caselist()
#
# for test in alltestnames:
#     testsuite.addTest(unittest.makeSuite(test))


filename = os.path.abspath(os.path.join(os.path.abspath(__file__),"../testcase/report/result.html"))
fp = open(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description='用例执行情况')
runner.run(testsuite)