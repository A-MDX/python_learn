__author__ = 'A-mdx'


# -*- coding: utf-8 -*-

def f(x):
	return x * x


l = [1, 3, 5, 7, 8, 10, 12]
r = map(f, l)
print('next-->r',next(r))
print(list(r))

r = map(str, l)
print(list(r))

from functools import reduce


def add(x, y):
	return x + y


l = [1, 3, 5, 7, 8, 10, 12]
a = reduce(add, l)
print(a)


# 当然求和运算可以直接用 Python 内建函数sum()，没必要动用reduce。
# 但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
def fn(x, y):
	return x * 10 + y


a = reduce(fn, [9, 5, 3, 7, 2, 1])

print(a)

from functools import reduce


def str2int(s):
	def fn(x, y):
		return x * 10 + y

	def char2int(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

	return reduce(fn, map(char2int, s))


# s = input('come and say:')
# print(str2int(s))

# 使用更方便的lambda表达式
def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def str2int(s):
	return reduce(lambda x, y: x * 10 + y, map(char2num, s))


s = '56781'
print(str2int(s))


def name(s):
	str1 = ''
	str1 += s[0].upper()
	str1 += s[1:len(s)].lower()
	return str1


print(name('aLiSS'))


def normalName(l):
	return list(map(name, l))


l = ['adam', 'LISA', 'barT']
print(normalName(l))

from functools import reduce
def prod(l):
	def fn(x, y):
		return x * y

	return reduce(fn, l)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


from functools import reduce
s = 'sasd.asd'
print(s.split('.'))
ar = [1,2,3,4,8,7]
ar.reverse()
print('ar:',ar)

def str2float(s):
	def char2int(c):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]
	arr = s.split('.')
	print(arr)
	num1 = reduce(lambda x,y:x*10+y ,map(char2int,arr[0]))
	print(num1)
	ar2 = list(map(char2int,arr[1]))

	ar2.reverse()
	ar2.append(0)
	print('ar2:',ar2)

	num2 = reduce(lambda x,y:x/10+y,list(map(char2int,arr[1])).reverse().append(0))

	# num2 = reduce(lambda x,y:x/10+y,ar2)
	print(num2)
	return num1+num2

print(str2float('103.1415926'))
