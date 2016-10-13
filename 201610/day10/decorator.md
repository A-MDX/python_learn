# 装饰者

我们要增强函数的功能，但是不想更改函数的定义，这种在代码运行期间动态增加功能的方式，叫做‘装饰器’`Decorator`.

本质上，decorator是一个返回函数的高阶函数，且看使用方式：

```python
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

@log
def now():
	print('2016-10-12')

now()

# 结果如下：

2016-10-12
__name__: now
call now():
2016-10-12

```

`__name__`,是对象的属性，函数也是一个对象。还可以这样使用：

```python
now = log(now)
now()
```

### 装饰器本身传入参数

这样比较复杂，需要编写一个返回decorator的高阶函数：

```python
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

# 结果

#-------------------------------------
#<function log.<locals>.decorator.<locals>.wrapper at 0x01E95DF8>
#test now():
#2016-10-12 15:40

#--------------------------------------
#也可以这么写

now = log('test')(now)

```

### 修饰后的name属性会变

像上面一样，直接把结果函数放进去，就可以直接得到了一个修饰过的。**注意**，这样的`__name__`属性会变！

```python
print(now)
print(now.__name__)

# 结果：

<function log.<locals>.wrapper at 0x012E5D20>
wrapper

```

如果不想变，可以这样：

```python
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

# 结果

# <function now at 0x01435DF8>
# now

```

#### 而带参数的装饰器

```python
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

# 结果
# ---555555-------
# <function now at 0x01905ED0>
```

### 练习

1.请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

```python
import functools

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

# 结果：

# begin call
#   ---   ***   ---  apple
# end call
# <function hha at 0x01655DF8>

```

2.思考一下能否写出一个@log的decorator，使它既支持：
```python
@log
def f():
    pass
```

又支持这个：

```python
@log('execute')
def f():
    pass
```

答题了：

```python
# 根本没法完成，调用不一样，方法体是不一样的！
```
