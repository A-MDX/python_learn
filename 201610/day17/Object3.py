
from enum import Enum

Month  = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'Nov'))

for name,number in Month.__members__.items():
	print(name, ' => ',number,number.value)
	
from enum import  Enum,unique


class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6
	
print(Weekday.Sat)
print(Weekday(1))

for name, member in Weekday.__members__.items():
	print(name, ' => ', member)

# 学这个python学的有点累了。
