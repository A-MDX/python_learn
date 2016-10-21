
# 1. try catch

try:
	print('try')
	r = 10 / 0
	print('result: ', r)
except ZeroDivisionError as e:
	print('except: ', e)
finally:
	print('finally...')
print('END')

# try
# except:  division by zero
# finally...
# END

print('-----------------')

try:
	print('try...')
	r = 10/5
	print('result :', r)
except ValueError as e:
	print('except :', e)
else:
	print('no error!')
finally:
	print('finally...')
print('end...')

# try...
# result : 2.0
# no error!
# finally...
# end...

print('--------------------------')

foo = lambda s : 10/int(s)
bar = lambda s : foo(s)*2
def main():
	try:
		bar('0')
	except Exception as e:
		print('Error : ',e)
	finally:
		print('finally...')

# main()

def main():
	bar('0')

# main()
 
# Traceback (most recent call last):
# --------------------------
#   File "C:/Users/A-mdx/PycharmProjects/python_learn/201610/day21/tryCatch1.py", line 56, in <module>
#     main()
#   File "C:/Users/A-mdx/PycharmProjects/python_learn/201610/day21/tryCatch1.py", line 54, in main
#     bar('0')
#   File "C:/Users/A-mdx/PycharmProjects/python_learn/201610/day21/tryCatch1.py", line 42, in <lambda>
#     bar = lambda s : foo(s)*2
#   File "C:/Users/A-mdx/PycharmProjects/python_learn/201610/day21/tryCatch1.py", line 41, in <lambda>
#     foo = lambda s : 10/int(s)
# ZeroDivisionError: division by zero

# 3. 记录错误

import logging

foo = lambda s : 10/int(s)
bar = lambda s : foo(s)*2
def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)
		
main()
print('end')
# ERROR:root:division by zero
# Traceback (most recent call last):
#   File "C:/Users/A-mdx/PycharmProjects/python_learn/201610/day21/tryCatch1.py", line 78, in main
#     bar('0')
#   File "C:/Users/A-mdx/PycharmProjects/python_learn/201610/day21/tryCatch1.py", line 75, in <lambda>
#     bar = lambda s : foo(s)*2
#   File "C:/Users/A-mdx/PycharmProjects/python_learn/201610/day21/tryCatch1.py", line 74, in <lambda>
#     foo = lambda s : 10/int(s)
# ZeroDivisionError: division by zero
# end
	
# 4.抛出错误 raise

class FooError(ValueError):
	print('FooError...')
	pass

def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value: %s' % s)
	return 10/n

foo('0')

def bar():
	try:
		foo('0')
	except Exception as e:
		print('except...')
		raise     # 这个等于，原封不动的向上抛出
	
bar()
	
