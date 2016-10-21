
# 1.assert
def foo(s):
	n = int(s)
	assert n != 0, 'n is zero'
	return n/10

main = lambda  : foo('0')
# main()
# Traceback (most recent call last):
#   ...
# AssertionError: n is zero

# 2. logging
import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n=%d' % n)
print(10/n)
