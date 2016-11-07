
# 线程

一个单核电脑怎么同时处理多个任务？

分为时间片，一个时间片里，运行一个任务，时间一到，立马终止，并开始进行其他任务。

时间片的间隔很短，但好多任务都运行了。就跟同步运行一样。

python 支持多线程。

要让Python程序实现多进程（`multiprocessing`），我们先了解操作系统的相关知识。

Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。

### os 不支持ｗｉｎｄｏｗｓ，我们可以用别的multiprocessing

```python
from multiprocessing import Process

# 子进程执行的代码

def run_proc(name):
	print('Run child process %s (%s)...' % (name,os.getpid()))
	
if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Process(target=run_proc, args=('test',))
	print('Child process will start.')
	p.start()
	p.join()
	print('Child process end.')
```

### 2.若启动大量线程，可以使用pool

看代码片段 `pool1`

### 3.子线程

很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。

subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。

下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：

看代码 `subprocess1`