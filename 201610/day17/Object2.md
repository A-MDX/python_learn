# python object 高级编程

### 1.使用__slots__

如果我们想要限制实例的属性怎么做？比如只允许使用`（name,age）`

这样子：

```python
class Student(object):
	__slots__ = ('name','age')  # 用tuple定义允许绑定的属性名称

# 这样就只允许(name,age)这两个属性了

```

**注意**，这个只对当前子例有效，对于**继承子类**无效！

### 2.使用@property

```python
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

```

@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作

**property**,简单来讲，允许了.属性的方式设置方法。

##### 练习

请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

```python
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
s.resolution   # 1920.00 * 1080.00
```

### 3.多重继承

在定义类的时候，可以使用多重继承，通常我们用来添加新功能！

若需要混入额外的功能，通过多重继承就可以实现。这种设计通常成为`MixIn`

```python
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
```

### 4.定制类

就是类似于`__slots__`,`__len__`,我们可以使用这类特殊变量或者函数性定制类。

#### 4.1 __str__

实现print()调用，更加美观，

```python
class Student(object):
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return 'Student object (name : %s)' % self.name
	__repr__ = __str__  # 返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
	
a = Student('bbq')
print(a)   # Student object (name : bbq)
```

#### 4.2 __iter__

如果一个类想被用于`for ... in`循环，
类似`list`或`tuple`那样，就必须实现一个`__iter__()`方法，
该方法返回一个迭代对象，
然后，Python的for循环就会不断调用该迭代对象的`__next__()`方法拿到循环的下一个值，
直到遇到`StopIteration`错误时退出循环。

```python

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
	
```

#### 4.3 __getitem__

这个实现了，可以直接通过下标访问数列的任意一级了。

```python
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
```

但是如果中括号里的是切片，则需要重新定义:

```python
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

```

+ 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
+ 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
+ 没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的;
+ 通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口