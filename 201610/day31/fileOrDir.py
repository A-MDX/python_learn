__author__ = 'a-mdx'
# -*- coding: utf-8 -*-

import os

def prDir(di):
	a = [x for x in os.listdir(di)]
	print(di,' -> ',a)
	for x in a:
		if os.path.isdir(di+'\\'+x):
			prDir(di+'\\'+x)
	
	
ad = input('adress ? -> ')
print(ad)
if not os.path.isdir(ad):
	print(r'It\'s not a dir -> %s' % ad)
else:
	prDir(ad)
	
	
# 运用递归完美的完成了。
