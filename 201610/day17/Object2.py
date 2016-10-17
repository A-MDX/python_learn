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

