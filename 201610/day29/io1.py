__author__ = 'A-mdx'
# -*- coding: utf-8 -*-

# 1.文件读写

f = open('E:/test/pw.txt','r')    # 'r' 表示读
f.read()
f.close()

# io容易发生io异常，我们可以使用try...finally...来

try:
	f = open("e:/test/pw.txt",'r')
	print(f.read())
finally:
	f.close()
	
# 这是不是很麻烦，我们可以使用更加简单的，使用with语句

with open('e:/test/pw.txt','r') as f :
	print(f.read())
	
	
