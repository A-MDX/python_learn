__author__ = 'A-mdx'

# 1.类创建与使用
class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score

	def print_score(self):
		print('name: %s,score: %0.2f.' % (self.name,self.score))

	# 这不就是java中的toString()方法嘛。
	def __str__(self):
		return 'name : %s --> score : %0.2f .' % (self.name,self.score)

alex = Student('Alex Mdx',99.99)
dj = Student('Deji Li',60.00)
alex.print_score()
dj.print_score()
print(alex)

class Wifi(object):
	def __init__(self,name,pwd):
		self.name = name
		self.pwd = pwd

	def check(self):
		if self.pwd == self.name:
			return True
		return False

a1 = Wifi('abc','d')
print(a1.check())

# 2.类详解

# 3.私有属性

print(alex.name,alex.score) # 可以只有访问！
alex.name = 'Madx' # 可以随意修改
print(alex)

# Alex Mdx 99.99
# name : Madx --> score : 99.99 .

class Student(object):
	def __init__(self,name,score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print('name: %s ,score: %0.2f' % (self.__name,self.__score))

alex = Student('Alex Ma',99.66)
print(alex) # <__main__.Student object at 0x01F9ED10>
# print(alex.__name) # AttributeError: 'Student' object has no attribute '__name'
alex.print_score()   # name: Alex Ma ,score: 99.66

print(alex._Student__name) # 可以在前面加下划线类名访问，还是可以的，但是不建议！

### 继承与多态

class Animal(object):
	def run(self):
		print('Animal is running!')

class Dog(Animal):
	pass
class Cat(Animal):
	def run(self):
		print('Cat is running!')
	pass

dog1 = Dog()
dog1.run()
cat1 = Cat()  # Animal is running!
cat1.run()       # Cat is running!

print(dog1)
print(type(dog1))
print(type(abs))

print(dir(dog1))

### 练习

# 这个python还真是鸭子类型啊。

class Word(object):
	def __init__(self,text):
		self.text = text
	def equals(self,word2):
		return self.text.lower() == word2.lower()
	def equals2(self,word2):
		return self.text.lower() == word2.text.lower()

a = Word('asd')
result = a.equals('bbq')
print(result)

b = Word('asd')
result = a.equals2(b)
print(result)
