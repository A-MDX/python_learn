__author__ = 'A-mdx'
# -*- coding: utf-8 -*-

import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code: ',r)
print('你好。。我是谁。。')