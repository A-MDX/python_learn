__author__ = 'A-mdx'
# -*- coding: utf-8 -*-

import json

class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score
	
s = Student('Bill',15,99)
# print(json.dumps(s))      # 错误的原因是Student对象不是一个可序列化为JSON的对象。

# 因为不知道怎么将一个对象转换为json对象，我们可以传入一个参数,可选参数default就是把任意一个对象变成一个可序列为JSON的对象

def student2dict(std):
	return {
		'name':std.name,
		'age':std.age,
		'score':std.score
	}

# 这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON

print(json.dumps(s,default=student2dict))

# 我们可以偷个懒，把任意class的实例变为dict

class Teacher(object):
	def __init__(self,name,age,salary):
		self.name = name
		self.age = age
		self.salary = salary
		

t = Teacher('Wang',25,5200)

# look，我们直接传入这个参数就好。我们可以偷个懒，把任意class的实例变为dict：

print(json.dumps(t, default= lambda obj:obj.__dict__))

# 再看看JSON反序列化

def dict2student(d):
	return Student(d['name'],d['age'],d['score'])

json_str = '{"age":18,"score":88,"name":"Nike"}'

print(json.loads(json_str,object_hook=dict2student))  # <__main__.Student object at 0x01E16B30>
