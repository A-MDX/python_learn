# 文件与文件夹的操作

### os

```python
>>> import os
>>> os.name  查看操作系统

'nt'   # 代表win

>>> os.environ
environ({'VERSIONER_PYTHON_PREFER_32_BIT': 'no', ...})

>>> os.environ.get('PATH')
'/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/mysql/bin'
>>> os.environ.get('x', 'default')
'default'
```

### 操作文件与文件夹

```python
>>> os.path.abspath('.')
'C:\\Users\\A-mdx\\PycharmProjects\\python_learn'

>>> os.path.join('E:/test','testDir')
'E:/test\\testDir'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
>>> os.mkdir('E:/test/testDir')  #创建
>>> os.rmdir('e:/test/testDir')  # 删除

>>> os.path.split('e:/test/apple.md')
('e:/test', 'apple.md')
>>> os.path.split('e:/test/day04')
('e:/test', 'day04')
>>> os.path.splitext('e:/test/apple.md')
('e:/test/apple', '.md')


```

最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：

```python
>>> [x for x in os.listdir('.') if os.path.isdir(x)]
['.git', '.idea', '201610']

>>> os.path.abspath('.')
'C:\\Users\\A-mdx\\PycharmProjects\\python_learn'
>>> [x for x in os.listdir('C:\\Users\\A-mdx\\PycharmProjects\\python_learn\\201610') if os.path.isdir(x)]
[]
>>> [x for x in os.listdir('C:\\Users\\A-mdx\\PycharmProjects\\python_learn\\201610') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
[]

```