# 文档测试

`python`中有内置的`文档测试`模块可以直接提取注释中的代码并执行测试。

`doctest`严格按照python交互命令行的输入与输出来判断结果是否正确，可以用`...`
表示中间一大段烦人的输出。

```

def abs(n):
	'''
	Function to get absolute value of number.
	
	Example:
	
	>>> abs(1)
	1
	>>> abs(-1)
	1
	>>> abs(0)
	0
	'''
	return n if n >= 0 else (-n)

print(abs(-19))

```

一般情况下，如果什么都不输出，就表示结果是对的。

让我们用doctest来测试上次编写的Dict类：

```

class Dict(dict):
	'''
	Simple dict but also support access as x.y style.
	
	>>> d1 = Dict()
	>>> d1['x'] = 100
	>>> d1.x
	100
	>>> d1.y = 200
	>>> d1[y]
	200
	>>> d2 = Dict(a= 1,b=2,c='3')
	>>> d2.c
	'3'
	>>> d2['empty']
	Traceback (most recent call last)：
		...
	KeyError:'empty'
	>>> d2.empty
	Traceback(most recent call last):
		...
	AttributeError:'Dict' object has no attribute 'empty'
	
	'''
	def __init__(self,**kw):
		super(Dict,self).__init__(**kw)
		
	def __getattr__(self, item):
		try:
			return self[item]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'" % item)
		
	def __setattr__(self, key, value):
		self[key] = value
		
if __name__  == 'main':
	import doctest
	doctest.testmod()
	
```