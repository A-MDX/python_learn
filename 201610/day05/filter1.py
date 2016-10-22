__author__ = 'A-mdx'
# -*- coding: utf-8 -*-

def is_odd(x):
	return x%2 == 0

l = [list(range(11))]
print(l)

print(list(filter(is_odd, [1,2,3,4,5,6,7,8,9])))

def not_empty(s):
	return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '] )))

print('--------------')

def odd_iter():
	n = 1
	while True:
		n += 2
		yield n

def not_divisiable(n):
	return lambda x : x%n != 0

def primes():
	yield 2
	it = odd_iter() # 初始化序列
	while True:
		n = next(it) # 返回序列第一个数
		yield n
		it = filter(not_divisiable(n),it)


for n in primes():
	if n < 10:
		print(n)
	else:
		break


print('----------------------------------------------------')

x = '456789'
x = [s for s in x]
print(x)
tmp = x[:]  # 这样复制
tmp.reverse()
print(tmp)

def creat_num():
	n = 12
	while n < 100000:
		yield n
		n += 1

def check(x):
	x = str(x)
	x = [s for s in x]
	tmp = x[:]
	tmp.reverse()
	if x == tmp:
		return True
	else:
		return False

def hui_num():
	n = 11
	cn = creat_num()
	while True:
		yield n
		cn = filter(check,cn)
		n = next(cn)

l = [x for x in hui_num() if x < 10000]
print(l)  # 第一种

out = filter(check , range(10,1000))   # 第二种方法
print(list(out))
