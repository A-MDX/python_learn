__author__ = 'A-mdx'
# -*- coding: utf-8 -*-

a = sorted([36, 5, -12, 9, -21])
print(a)

li = [36, 5, -12, 9, -21,1,-9,-3,-11]
print(sorted(li,key=abs))

L = [('Bob', 75),('Lisa', 88), ('Adam', 92), ('Bart', 66)]

def by_name(l):
	return l[0]

print(sorted(L,key=by_name))

def by_score(l):
	return l[1]

L2 = sorted(L,key=by_score,reverse = True)
print(L2)


