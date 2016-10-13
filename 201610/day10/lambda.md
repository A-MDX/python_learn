# 关于匿名函数

当我们传入参数的时候，有些时候，不需要显式定义函数，直接传入匿名函数比较方便。

```python

f = map(lambda x: x*x+1,[x for x in range(5)])
print(list(f))

print('------------------------------------------------')

def fc(x):
	return x*x+1

f = map(fc,[x for x in range(5)])
print(list(f))

```

结果都是一样的，但可以明显看到，使用lambda表达式构建匿名函数可以更为方便，并且没有对代码环境造成污染。

```python
>>> f = lambda x : x +3
>>> f(2)
5
>>> f = lambda x : x*x +1
>>> f(8)
65
```

可以直接使用这种方式来构建函数，很方便。

### 小结

+ 可以将一些简单的方法使用匿名函数来表示，python对于lambda的支持不多；
+ 使用这个，可以减少代码量，清晰，一目了然。
