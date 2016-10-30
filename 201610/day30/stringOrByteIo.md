# stringIO 和 byteIO

### StringIO

很多时候，数据读写不一定是文件，也可以在内存中读写。

`StringIO` 就是在内存中读写`str`。

下面来看看事例：

```python
>>> from io import StringIO
>>> f = StringIO()
>>> f.write('hello')
5
>>> f.write(' ')
1
>>> f.write('world!')
6
>>> print(f.getvalue())   # getvalue()直接获取写入后的str
hello world!

```

上面是写，下面来段读操作：

```python
from io import StringIO

f = StringIO('Hello!\nHi!\nGoodBye!')
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())
	
# Hello!
# Hi!
# GoodBye!

```

### byteIO

要操作二进制数据，只能用这个。

```
>>> from io import byteIO
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ImportError: cannot import name 'byteIO'
>>> from io import bytesIO
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ImportError: cannot import name 'bytesIO'
>>> from io import BytesIO
>>> f = BytesIO()
>>> f.write('中文'.encode('utf-8'))
6
>>> print(f.getvalue())
b'\xe4\xb8\xad\xe6\x96\x87'

# 注意，要分清楚大小写。。
```

看看读取

```python
>>> f2 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
>>> f2.read()
b'\xe4\xb8\xad\xe6\x96\x87'
```

内存的读写，目前尚不知道作用。