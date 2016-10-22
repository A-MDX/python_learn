__author__ = 'A-mdx'
# code=utf-8

arr = ['asd', 456, True, 'OK']
print(arr)

arr1 = ('bbq', 'test', 132, arr)
print(arr1)


def diy_max(a, b):
	if a > b:
		return a
	elif a == b:
		return a
	else:
		return b


print(max(7, 7))


def hello(a):
	print('hello %s!' % a)


hello('哦')


def for_jie(n):
	a = 1
	for i in range(1, n + 1):
		a *= i
	return a


# num = input('来输入一个数字: ')
# num = int(num)
# a = for_jie(num)
# print('%d 的 阶乘是 %d' % (num, a))

for i in (1, 5, 9, 76, 4, 3, 55, 66, 77):
	if i % 2 == 0:
		continue
	print(i)
# let get some learn

dic = {'xi\'an': 10, 'xian': 20}
print(dic['xian'])
dic['apple'] = 5800
dic['orange'] = 1200

dic.pop('orange')
print(dic.keys())
if 'orange' in dic:
	print('xxx')
else:
	print('yyy')

print(diy_max)

a = 'asdfghjkl'
b = a.replace('s', ' FUCK ')
print(a, '\n', b)


def calc(*num):
	sum1 = 0
	for i in num:
		sum1 += i * i
	return sum1


a = calc(1, 2, 3, 487, 65, 1, 54, 6, 7, 9, 4)
print(a)

b = [1, 5, 7, 6, 7, 8, 1, 3, 5]
a = calc(*b)
print('second', a)


def jie(num):
	if num is 1:
		return 1
	return num * jie(num - 1)


print(jie(5))


# 尾递归
def jie1(num):
	return jie_init(num, 1)


def jie_init(num1, sum1):
	if num1 == 1:
		return sum1
	return jie_init(num1 - 1, sum1 * num1)


print('it is use 尾递归', jie1(5))


def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
        return
    move(n-1, a, c, b)
    print('move', a, '-->', c)
    move(n-1, b, a, c)

move(4, 'A', 'B', 'C')
