__author__ = 'A-mdx'
# -*- coding: utf-8 -*-

import threading,multiprocessing

def loop():
	x = 0
	while True:
		x = x^1
	
for i in range(multiprocessing.cpu_count()):
	t = threading.Thread(target=loop)
	t.start()


# 写个死循环，看看某些东西，比如cpu的运算量

