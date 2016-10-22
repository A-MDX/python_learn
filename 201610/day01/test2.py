__author__ = 'A-mdx'
# -*- coding: utf-8 -*-

ls = [x * x for x in range(1, 21) if x % 2 == 0]
print(ls)

ls = [x + y for x in 'asd' for y in 'zxc']
print(ls)

ar = ['hello', 'apple', 'smart', True, None, 123, 'orange']
ar = [s for s in ar if isinstance(s, str)]
arr = []
for k in ar:
	s1 = ''+k[0].upper()
	a = 1
	for s in k:
		if a == 1:
			a += 1
			continue
		else:
			s1 += s
			a += 1
	arr.append(s1)
print(arr)
