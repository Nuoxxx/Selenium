import sys
import unittest

# sys.path.append(".")
import youdao
import baidu

testsuite = unittest.TestSuite()

testsuite.addTest(unittest.makeSuite(baidu.Baidu))
testsuite.addTest(unittest.makeSuite(youdao.Youdao))

runner = unittest.TextTestRunner()
runner.run(testsuite)