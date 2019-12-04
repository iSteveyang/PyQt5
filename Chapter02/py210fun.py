# -*- coding: utf-8 -*-

# lambda是一个表达式，而不是一个语句，
# 它能够出现在Python语法不允许def出现的地方。
# 作为表达式，lambda返回一个值（即一个新的函数）。
fun1 = lambda x,y : x + y  
print('fun1(2,3)=' , fun1(2,3))

fun2 = lambda x: x*2
print('fun2(4)=' , fun2(4) )
