# -*- coding: utf-8 -*-
 
class MyClass(object):
	def __init__(self):
		self._param = None  

	# “将Python定义的函数“当作”属性访问”
	@property
	def param(self):  
		print( "get param: %s" % self._param)
		# 首先进入inintial, 属性_param = None, 故返回None
		return self._param  

	@param.setter
	# 参数"10"传入，调用setter
	def param(self, value):  
		print( "set param: %s" % self._param )
		self._param = value  
	 
	@param.deleter  
	def param(self):  
		print( "del param: %s" % self._param)
		del self._param  

if __name__ == "__main__":
	cls = MyClass()
	cls.param = 10
	print("current param : %s " % cls.param )
	# 此时cls.param 为MyClass类实例cls函数的属性
	del cls.param
