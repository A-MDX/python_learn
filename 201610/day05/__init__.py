__author__ = 'A-mdx'
# -*- coding: utf-8 -*-

def add(x, y, f):
	return f(x) + f(y)

a = add(15,-9,abs)
print(a)

import math

a = add(13,-8,math.cos)
print(a)

