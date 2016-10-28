# create by A-mdx

def fact(n):
	'''
	this is a fact doc test:
	
	>>> fact(1)
	1
	>>> fact(0)
	0
	>>> fact(-2)
	Traceback (most recent call last):
		...
	ValueError
	>>> fact(5)
	20
	'''
	if n < -1:
		raise ValueError()
	if n == 1:
		return 1
	return n * (n-1)



