__author__ = 'A-mdx'

# 这就是懒惰加载
def lazy_sum(*args):
	def sum():
		ax = 0
		for i in args:
			ax += i
		return ax
	return sum

a = lazy_sum(1,5,4,8,9,4,6,3,1,2,7)
print(a)
print('a() : %d ' % a())
