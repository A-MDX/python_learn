__author__ = 'A-mdx'


# -*- coding: utf-8 -*-


def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, b + a
		n += 1
	return 'done'


print(fib(8))


def gfib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield (b)
		a, b = b, a + b
		n += 1
	return 'done'


# <generator object gfib at 0x0118BCC0>
print(gfib(5))

# 1
# 1
# ----------------------------
# 2
# 3
# 5
g = gfib(5)
print(next(g))
print(next(g))
print('----------------------------')
for k in g:
	print(k)

# g 1
# g 1
# g 2
# g 3
# g 5
g = gfib(5)
while True:
	try:
		a = next(g)
		print('g', a)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break


# 杨辉三角
def yan(n):
	a = 0
	l = [1]
	while a < n:
		yield (l)
		l = [l[x] + l[x + 1] for x in range(len(l) - 1)]
		l.insert(0, 1)
		l.append(1)
		a += 1


g = yan(6)
for k in g:
	print(k)
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]

# test2
print('-------------------------------')


def yan2(num):
	N = [1]
	a = 0
	while a < num:
		yield(N)
		N.append(0)
		N = [N[x - 1] + N[x] for x in range(len(N))]
		a += 1

g = yan2(5)
for k in g:
	print(k)