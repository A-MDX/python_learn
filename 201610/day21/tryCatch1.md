# 错误，调试和测试

来学习一下`python`中的异常处理机制。

### 1.try ... except... finally...

```
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
```

跟**java**中的`try-catch-finally`很相似，也很简单啊。
只不过是把`catch`变成了`except`了，可以有多个`except`。

可以在`except`后面加个`else`，当没有错误的时候，会执行这个`else`

```
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
```

### 2.调用堆栈

如果没有`try-except`,它会一直向上抛，最后被python解释器捕获。

```

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

main()

def main():
	bar('0')

main()
 
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

```

### 3.记录错误

如果不捕获错误，python可以打印错误堆栈，但是程序也结束了。
既然我们能抓住错误，分析打印出来，让程序继续执行就好。

```
import logging

foo = lambda s : 10/int(s)
bar = lambda s : foo(s)*2
def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)
		
main()

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

```

### 4.抛出错误

我们可以自己简历错误类，自己抛出去；这个和`java`中的`throw`很像。


