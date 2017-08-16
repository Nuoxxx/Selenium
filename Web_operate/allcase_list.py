import sys
import unittest
import HTMLTestRunner

sys.path.append("\Selenium_Learn")

from Selenium_Learn.Web_operate.ceses import start_baidu
from Selenium_Learn.Web_operate.ceses import youdao

def caselist():
    #用该list专门用于添加测试用例
    alltestnames = [start_baidu.Baidu, youdao.Youdao]
    print(sys.path)
    print("Success read case list!!!")

    return alltestnames