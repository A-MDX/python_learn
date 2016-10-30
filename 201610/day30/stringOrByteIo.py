__author__ = 'A-mdx'
# -*- coding: utf-8 -*-

from io import StringIO

f = StringIO('Hello!\nHi!\nGoodBye!')
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())
	
# Hello!
# Hi!
# GoodBye!
