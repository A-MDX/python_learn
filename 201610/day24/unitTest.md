# 单元测试

用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。

### 注意

+ 以test为开头，例如`test_ok`；
+ `setUp` 和 `tesrDown` 就是java中的`before`和`after`。
+ 要引入`unittest`包；
+ 建立继承类，在类中写方法
+ 在后面可以直接`unittest.main()`方法直接运行。

以下是源码，比较简单：

```python

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

```

