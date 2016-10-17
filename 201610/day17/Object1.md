# python object

> 面向对象，春暖花开

### 1.先看一个实例

在python中，类，以及对象的使用，这样子：
```python
class Stud(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score
	def prints(self):
		print('std name : %s ,score : %0.2f ' % (self.name,self.score))

xm = Stud('xiao ming',18.0)
xm.prints()
```

### 2.详解

+ 先使用`class`来定义类；
+ 看类名里面的`object`，这个表示类从哪里继承下来；
+ 和普通函数相比，类定义只有一点不同，就是第一个参数永远是`self`，调用时，不用传;
+ 这和`java`比较像；

### 3.私有属性

在python中，使用`__`两个下划线，就变成了私有变量。

```python
# 3.私有属性

print(alex.name,alex.score) # 可以只有访问！
alex.name = 'Madx' # 可以随意修改
print(alex)

# Alex Mdx 99.99
# name : Madx --> score : 99.99 .

class Student(object):
	def __init__(self,name,score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print('name: %s ,score: %0.2f' % (self.__name,self.__score))

alex = Student('Alex Ma',99.66)
print(alex) # <__main__.Student object at 0x01F9ED10>
# print(alex.__name) # AttributeError: 'Student' object has no attribute '__name'
alex.print_score()   # name: Alex Ma ,score: 99.66

```

可以自己给添加上get`()`,`set(s)`方法!

### 4.继承与多态

```python
class Animal(object):
	def run(self):
		print('Animal is running!')

class Dog(Animal):
	pass
class Cat(Animal):
	def run(self):
		print('Cat is running!')
	pass

dog1 = Dog()
dog1.run()
cat1 = Cat()  # Animal is running!
cat1.run()       # Cat is running!
```

由上面可以看出，继承之后，可以直接得到原来的方法。这个和`java`的继承与多态类似，但没那么复杂。

> **鸭子类型**:动态类型里，不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那么就可以被看作为鸭子。

### 5.判断对象类型

#### 5.1 使用type()

用法简单，只要调用`type(obj)`方法就行了。

但如果要判断一个对象是否是函数，可以这样：

```python
Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
>>> import types
>>> def fn():
... 	pass
...
>>> type(fn) == types.FunctionType
True
>>> type(abs) == types.BuiltinFunctionType
True
>>> type(lambda x : x+1) == types.LambdaType
True
>>> type((x for x in range(10))) == types.GeneratorType
True
```

#### 5.2 使用isinstance()

这个比`type()`方法，可以用来判断多态继承等。

#### 5.3 使用dir()

若要获得一个对象的所有属性和方法，可以使用`dir()`方法

正确查看方法

```python
def readImage(fp):
	if(hasattr(fp,'read'):
		return readDate(fp)
	return None

使用 hasattr(obj,'x') 还判断是否含有方法，
使用 setattr（obj,'y',10） 设置一个属性
使用 getattr(obj,'x') 获取一个属性
```

### 6. 实例属性

在类定义里写就好，看例子：

```python
>>> class Student(object):
... 	name = "Student"
...
>>> a = Student()
>>> a.name
'Student'
>>> a.name = 'Alex'   # 给实例绑定name属性
>>> a.name
'Alex'          # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
>>> Student.name
'Student'      # 但是类属性并未消失，用Student.name仍然可以访问
>>> del a.name   # 如果删除实例的name属性
>>> a.name
'Student'   # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了

```