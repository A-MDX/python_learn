# 模块，module

在python中，每一个`.py`都是一个模块。

### 关于使用模块的好处

+ 最大好处是提高的代码的可维护性；
+ 编写代码不用从零开始，当一个模块编写完毕，就可以被其他地方引用；
+ 避免名字与其他模块冲突，尽量不要与内置函数名字冲突，

### 为了避免模块名冲突，可以按目录来组织模块，避免冲突

**注意**，`__init__.py`这个文件是必须存在的，否则就被当作普通目录，而不是一个包。
`__init__.py`可以是空文件，也可以有python代码，因为其本身就是一个模块，模块名就叫文件夹的名字。

引用，这样：
```python
   com.madx.something
```