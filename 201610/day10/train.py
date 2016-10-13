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


print('--------------------------------------------------------')

def count():
	def fi(j):
		return lambda :j*j
	fs = []
	for i in range(1,4):
		fs.append(fi(i)) # 在这个地方，i被绑定了。
	return fs

ff = count()
print(ff)

