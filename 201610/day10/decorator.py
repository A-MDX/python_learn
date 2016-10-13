__author__ = 'A-mdx'


def now():
	print('2016-10-12')

now()

print('__name__:',now.__name__)

def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	return wrapper

now = log(now)
now()

print(now)
print(now.__name__)

print('-------------------------------------')

def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print('%s %s():'% (text, func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

@log('test')
def now():
	print('2016-10-12 15:40')

print(now)
now()

print('-----------------------------')

import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*arg,**kw):
		print('call %s():' % func.__name__)
		return func(*arg,**kw)
	return wrapper

@log
def now():
	print('2016-10-12 15:40')

print(now)
print(now.__name__)

# <function now at 0x01435DF8>
# now

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s %s():'% (text, func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

def now():
	print('---555555-------')

now = log('log')(now)
now()
print(now)
#
# ---555555-------
# <function now at 0x01905ED0>

print('------------------------------------------------')
# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

def hha(ok):
	print('  ---   ***   --- ',ok)

def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('begin call')
		func(*args,**kw)
		print('end call')
		return
	return wrapper

hha = log(hha)
hha('apple')
print(hha)

# begin call
#   ---   ***   ---  apple
# end call
# <function hha at 0x01655DF8>

print('------------------------------------------------------------')
