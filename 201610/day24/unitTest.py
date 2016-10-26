__author__ = 'A-mdx'
# -*- coding: utf-8 -*-

class Dict(dict):
	def __init__(self,**kw):
		super().__init__(**kw)
	
	def __getattr__(self, item):
		try:
			return self[item]
		except KeyError:
			raise AttributeError(r"'dict' object has no attribute '%s'" % item)
		
	def __setattr__(self, key, value):
		self[key] = value
		
# 为了编写单元测试，我们需要引入python自带的unittest模块。


