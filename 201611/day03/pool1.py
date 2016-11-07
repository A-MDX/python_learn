__author__ = 'A-mdx'
# -*- coding: utf-8 -*-

from multiprocessing import Pool
import os,time,random

# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：

def long_time_task(name):
	print('Run task %s (%s)...' % (name,os.getpid()))
	start = time.time()
	time.sleep(random.random()*3)
	end = time.time()
	print('Task %s run %0.2f second.' % (name, (end-start)))
	
if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task,args=(i,))
	print('Wait for all subprocess done...')
	p.close() # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
	p.join() # 等待子进程结束后再继续往下运行，通常用于进程间的同步
	print('All subprocesses done...')
