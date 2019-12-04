# -*- coding: utf-8 -*-

# 通常继承object类，是python历史遗留问题，本学习环境适用于python3.7
# 此地继承object类，是为解释类的动态特性熟悉property用法
# “定义了一个MyClass类，该类必须继承自object类”

class MyClass(object):
    def __init__(self):
        self._param = None

    def getParam(self):
        print( "get param: %s" % self._param)
        return self._param

    def setParam(self, value):
        print( "set param: %s" % self._param )
        self._param = value

    def delParam(self):
        print( "del param: %s" % self._param)
        del self._param

    param = property(getParam, setParam, delParam)

if __name__ == "__main__":
    # 在property中cls 是 MyClass 的实例化
    cls = MyClass()
    # cls.param = value 将触发 setter
    cls.param = 10
    # cls.param 将触发 getter
    print("current param : %s " % cls.param )
    # del cls.param 触发 deleter
    del cls.param
