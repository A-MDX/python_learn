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


import unittest

class TestDict(unittest.TestCase):
	
	def test_init(self):
		d = Dict(a=1,b='test')
		self.assertEqual(d.a,1)
		self.assertEqual(d.b,'test')
		self.assertTrue(isinstance(d,dict))
		
	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEqual(d.key,'value')
		
	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d )
		self.assertEqual(d.key,'value')
		
	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']
	
	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty
			
	def setUp(self):
		print('start....')
		
	def tearDown(self):
		print('end...')
			

if __name__  == '__main__':
	unittest.main()


