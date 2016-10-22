__author__ = 'A-mdx'
print('Hello,world')

print('Mr.Ma,hi time is %s ...' % '15:02')

print('zzxc',True,False)

for i in range(1,4):
    print('this is',i)

import math

print(math.e)

print(math.pi)

print('你好，世界')

print(math.cos(2*math.pi))

def chengfa():
    for i in range(1,10):
        st = ''
        for j in range(1,i):
            st += ' %d x %d = %d ' % (j,i,i*j)
        print(st)
chengfa()