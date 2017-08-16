import sys
import unittest
import HTMLTestRunner

sys.path.append("\test_case3")
from test_case3 import youdao
from test_case3 import baidu

def caselist():
    alltestnames = [baidu.Baidu, youdao.Youdao]
    print(sys.path)
    print("Success read case list!!!")

    return alltestnames