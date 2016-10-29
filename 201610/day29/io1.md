# IO 编程

IO，就是输入与输出，`Stream` 流。

### 1. 文件读写

#### 1.1 读文件

```python
>>> f = open('E:/test/pw.txt','r') 
>>> f
<_io.TextIOWrapper name='E:/test/pw.txt' mode='r' encoding='cp936'>
>>> f.read()

```

`r`表示读，可以使用`f.read()`来一次性全部读取，最后就要关闭，`f.close()`

```python
# io容易发生io异常，我们可以使用try...finally...来

try:
	f = open("e:/test/pw.txt",'r')
	print(f.read())
finally:
	f.close()
	
# 这是不是很麻烦，我们可以使用更加简单的，使用with语句

with open('e:/test/pw.txt','r') as f :
	print(f.read())
	
# ------------------------------------------
	
>>> f.read()
'hello,Mr.Ma.\nyou are not alone.\nYes,just keep going!\n'
>>> for line in f.readline():
... 	print(line.strip()) # 去掉‘/n’


```

二进制文件

```python
>>> f = open('/Users/michael/test.jpg', 'rb')
>>> f.read()
b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节

```

字符编码

要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：

```python
>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
>>> f.read()
'测试'

# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，
# 因为在文本文件中可能夹杂了一些非法编码的字符。
# 遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。
# 最简单的方式是直接忽略：
>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

```

#### 1.2 写文件

```python
>>> f = open('e:/test/pw2.txt','w')
>>> f.write('Hello,Me!')
9
>>> f.close()

# 使用with方便点

with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')

```

#### 1.3 小结

在python中，使用`open()`函数来完成io，使用`with`语句是个好习惯。
