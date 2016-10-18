__author__ = 'A-mdx'


# 1.使用__slots__
class Student(object):
	__slots__ = ('name','age')  # 用tuple定义允许绑定的属性名称

# 这样就只允许(name,age)这两个属性了

# 2.使用@property
class Student(object):
	def get_score(self):
		return self._score
	def set_score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an Integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0-100!')
		self._score = value

a = Student()
# print(a.set_score('x'))
# print(a.set_score(955))
a.set_score(85)
print(a.get_score())

#  我们来看看@property的用法
class Student(object):

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an Integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0-100!')
		self._score = value

s = Student()
# s.score = 105
# s.score = 'asd'
s.score = 100
print(s.score)

# 在看看定义只读属性
class Person(object):

	@property
	def birth(self):
		return self._birth

	@birth.setter
	def birth(self,value):
		self._birth = value

	@property
	def age(self):
		return 2016-self._birth

p = Person()
p.birth = 1986
print(p.age,p.birth,p._birth)
# p.age = 15  # 报错。

# 练习
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

class Screen(object):
	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self,value):
		if not isinstance(value,int):
			raise TypeError('value -> %s is not a Integer!' % value)
		self.__width = value

	@property
	def height(self):
		return self.__height

	@height.setter
	def height(self,value):
		if not isinstance(value,int):
			raise TypeError('this is not a number -> %s' % value)
		self.__height = value

	@property
	def resolution(self):
		print('%.2f * %.2f' % (self.__width,self.__height))

s = Screen()
s.width = 1920
s.height = 1080
s.resolution

# 3.多重继承

# 如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
class runnableMixIn(object):
	def run(self):
		print('Running...')

class WangwangMixIn(object):
	def wang(self):
		print('wang wang wang!')

class Animal(object):
	pass

class Dog(Animal,runnableMixIn,WangwangMixIn):
	pass

dog = Dog()
dog.run()
dog.wang()

# 4. 定制类

# 4.1
class Student(object):
	def __init__(self,name):
		self.name = name
	
	def __str__(self):
		return 'Student object (name : %s)' % self.name
	
	__repr__ = __str__  # 返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
	
	
a = Student('bbq')
print(a)   # Student object (name : bbq)

# 4.2

class fib(object):
	def __init__(self):
		self.a, self.b = 0,1
	
	def __iter__(self):
		return self
	
	def __next__(self):
		self.a, self.b = self.b, self.a+self.b
		if self.a > 100:
			raise StopIteration();
		return self.a

for i in fib():
	print(i)
	

print('---------------------------------------')
# 4.3

class Fib(object):
	def __getitem__(self, item):
		a, b = 1, 1
		for x in range(item):
			a, b = b, a+b
		return a

f = Fib()
print(f[1])   # 1
print(f[20])  # 10946
print(f[11])  # 144

class Fib(object):
	def __getitem__(self, item):
		if isinstance(item,int):
			a, b = 1, 1
			for x in range(item):
				a, b = b, a + b
			return a
		if isinstance(item,slice):
			start = item.start
			stop = item.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a+b
			return L
		
f = Fib()
print(f[0:5])
print(f[6:10])
