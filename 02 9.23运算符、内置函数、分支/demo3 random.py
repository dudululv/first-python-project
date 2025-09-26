import random 
print(random.randint(1,2))
random.seed(2)
a=random.randint(1,100)
print(a)
random.seed(1999999999999999999999999999)
print(a)
random.seed('中文随机量')
print(a) #只改了 seed，但没重新生成随机数，a 一直没变。要想让 a 跟着变化，必须在每次 seed(...) 后重新调用一次 random.randint(...)。