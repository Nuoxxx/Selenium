import sys
import unittest
import HTMLTestRunner

sys.path.append("\ceses")
from ceses import youdao
from ceses import start_baidu


def caselist():
    alltestnames = [start_baidu.Baidu, youdao.Youdao]
    print(sys.path)
    print("Success read case list!!!")

    return alltestnames