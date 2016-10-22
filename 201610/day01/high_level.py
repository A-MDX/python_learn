__author__ = 'A-mdx'
# -*- coding: utf-8 -*-

a = []
n = 1
while n <= 99:
	a.append(n)
	n += 2
print(a)

# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
r = []
for i in range(3):
	r.append(L[i])
print(r)

a = L[0:3]  # this is slice 切片
print(a)

b = L[:4]  # if start is 0,
print(b)

c = L[-3:-1]
print(c)

# 迭代key
dic = {'a': 15, 'b': 20, 'c': 15, 'd': True, 'e': 'axc'}
for key in dic:
	print(key,dic[key])

print('------------------------------------------------')

# 迭代value
for v in dic.values():
	print(v)

print('------------------------------------------------')

# 迭代key,value
for key,v in dic.items():
	print(key,v)

print('------------------------------------------------')

arr = ['az','bb','cd','ef']
for i,v in enumerate(arr):
	print(i,v)

print('------------------------------------------------')
arr = [(1,2),(2,5),(7,9),(0,1)]
for x,y in arr:
	print(x,y)

print('------------------------------------------------')
st = 'qwertyuiop'
for s in st:
	print(s)

print('------------------------------------------------')
from collections import Iterable
a = isinstance('asd',Iterable)
print(a)
b = isinstance([1,2,3],Iterator)
print(b)
c = isinstance(123456,Iterator)
print(c)