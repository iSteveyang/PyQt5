# -*- coding: utf-8 -*-
 
class MyCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量

    def __privateCountFun(self):
        print('这是私有方法')
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)
        
    def publicCountFun(self):
        print('这是公共方法')
        self.__privateCountFun()

if __name__ == "__main__":
    counter = MyCounter()
    counter.publicCountFun()
    # 测试私有方法被内部调用
    counter.publicCountFun()
    # 实例访问公共变量
    print ('instance publicCount=%d' % counter.publicCount)
    # 报错，实例不能访问私有变量
    # print (counter.__secretCount)

    # 类访问公共变量
    print ('Class publicCount=%d' % MyCounter.publicCount)
    # 报错，实例不能访问私有方法
    # counter.__privateCountFun()
