
class Apple(object):
	
	@property
	def name(self):
		return self.__name
	
	@name.setter
	def name(self,name):
		if isinstance(name, str):
			self.__name = name
		else:
			self.__name = 'null'

a = Apple()
a.name = 123
print(a.name)
a.name = 'apl'
print(a.name)


# 我们能写出这样的链式调用：Chain().users('michael').repos   GET /users/:user/repos

class Chain(object):
	def __init__(self,path = 'github'):
		self._path = path
	
	def __getattr__(self, item):
		return Chain('%s/%s' % (self._path,item))
	
	def users(self,name):
		return Chain('%s/%s' % (self._path,name))
	
	def __str__(self):
		return self._path
	
a = Chain().users('a-mdx').good.ok
print(a)
	
