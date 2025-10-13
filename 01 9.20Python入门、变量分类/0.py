'''
这是一个多行注释
其实只是一个字符串
但没有人用它
Python 没有真正的多行注释语法，只有单行注释 #
'''

print('\'' '1''')
print('''hello world''')

a="123456789"
for i in range(8,1,1):
    print(a[i])

print('='*20)
x=11
y=11
print(id(x),id(y),x is y)
m=12.1
n=12.1
print(id(m),id(n),m is n) #该项会在py文件与交互式环境中输出不同的结果
a=[1,2]
b=[1,2]
print(a is b)
print('='*20)

result = print("hello")  # print() 函数返回 None
print(result)  # 输出: None

input(None)
