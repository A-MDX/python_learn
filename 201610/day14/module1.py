__author__ = 'A-mdx'

import sys

def test():
    args = sys.argv
    if len(args)==1:
            print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

# 可以使用 _func ,_var 来定义 私有方法，或者变量，_ 这只是一种编程方式上的约定俗成。
def _hello1(name):
	print('hello %s' % name)

def _hello2(name):
	print('don\'t hello %s' % name)

def greeting(name):
	if len(name) > 3:
		_hello2(name)
	else:
		_hello1(name)

greeting('mdx')
greeting('madx')
