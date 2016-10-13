### 函数做为返回值

```python
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax += n
		return ax
	return sum

a = lazy_sum(5,6,97,1,3,46,4,12,45,21,11,34)
print(a)
print(a())

# 结果如下：

<function lazy_sum.<locals>.sum at 0x01C25CD8>
285

```
通过这个简单的程序我们可以看出：

+ 如果我们不需要立刻得到相关的结果，可以先返回一个函数，然后再调用这个函数即可；
+ 在这个例子中，我们在函数`lazy_sum`中定义了函数`sum`，并且内部函数`sum`可以引用外部函数`lazy_sum`的参数和局部变量，当`lazy_sum`返回函数`sum`时，相关参数和变量都保存在了返回的参数里，这就叫**闭包（Closure）**。
+ 还需要注意一点，当我们调用`lazy_sum()`时，每次的调用都会返回一个新的函数，即使传入的参数相同。

```python
a = lazy_sum(1,2,3,4,5,6)
b = lazy_sum(1,2,3,4,5,6)
print('a --> ',a)
print('b --> ',b)

print(a == b)

# 结果如下

a -->  <function lazy_sum.<locals>.sum at 0x01135198>
b -->  <function lazy_sum.<locals>.sum at 0x01135CD8>
False

```

### 关于闭包

**注意**返回的函数在其定义的内部引用了局部变量`args`,所以当一个函数返回一个函数后，其内部的局部变量还是会被新函数引用。

```python
def count():
	fs = []
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs

ff = count()
print(ff)

f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())

# 结果如下：

[<function count.<locals>.f at 0x01585198>, <function count.<locals>.f at 0x01585DB0>, <function count.<locals>.f at 0x01585DF8>]
9
9
9

```

**结果全是9**，原因就在于返回的函数引用了变量 `i`,这个变量并非立刻执行，而是等到所有运算完毕，此时的`i`已经变成了 **3** 。

#### 注意，闭包的时候，牢记，返回的函数不要引用任何循环变量，或者后续会发生变化的变量

如果一定要引用呢？方法就是再创建一个函数，用该函数的参数绑定循环变量当前的值，已绑定的参数值不会变了。

```python
def count():
	def fi(j):
		def g():
			return j*j
		return g
	fs = []
	for i in range(1,4):
		fs.append(fi(i)) # 在这个地方，i被绑定了。
	return fs

ff = count()
print(ff)

f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())

# 结果如下

[<function count.<locals>.fi.<locals>.g at 0x00B25F60>, <function count.<locals>.fi.<locals>.g at 0x00B25FA8>, <function count.<locals>.fi.<locals>.g at 0x00B47030>]
1
4
9

```

### 小结

+ 函数可以返回一个计算结果，也可以返回一个函数；
+ 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。
