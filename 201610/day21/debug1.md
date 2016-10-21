# debug 调试

程序一般都有错误，需要调试，一般用`print()`，这样很麻烦。

下面有几种很好的方法：

### 1.assert 断言

```
def foo(s):
	n = int(s)
	assert n != 0, 'n is zero'
	return n/10

main = lambda  : foo('0')
main()
# Traceback (most recent call last):
#   ...
# AssertionError: n is zero

```

+ java中似乎也有这个。
+ `assert`表达式 `n != 0 `应该是`True`，否则错误。
+ 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用`-0`参数来关闭assert

### 2. logging 

这个可以输入到文件。

```
import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n=%d' % n)
print(10/n)
```

+ 它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了;
+ logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

### 3. 使用ide调试

没啥说的，加断点。
