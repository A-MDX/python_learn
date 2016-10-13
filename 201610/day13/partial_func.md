# 偏函数

简单总结，`functions.partial` 的作用就是把一个函数的参数固定住，**等于设置默认值**，返回一个新函数，调用这个新函数会更加简单。

```python
__author__ = 'A-mdx'

num = '1234'
print(int(num))

print(int(num,base=8))

def int1(num):
	return int(num,base=8)

# 以上还要重新创建函数

# 使用麻烦，可以使用偏函数重新创建新的默认参数的函数

import functools
int2 = functools.partial(int,base=2)

print(int2)
print(int2('101100'))

# 1234
# 668
# functools.partial(<class 'int'>, base=2)
# 44
```
