__author__ = 'A-mdx'

f = map(lambda x: x*x+1,[x for x in range(5)])
print(list(f))

print('------------------------------------------------')

def fc(x):
	return x*x+1

f = map(fc,[x for x in range(5)])
print(list(f))
