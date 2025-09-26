f,g,h={2:4},{3:6},{4:8}
print(f+g+h)  #TypeError: unsupported operand type(s) for +: 'dict' and 'dict',说明+不可用于dict
u,i={2},{3}
print(u+i)  #TypeError: unsupported operand type(s) for +: 'set' and 'set',说明+不可用于set
a,b=1,'2'
print(a+b)  #unsupported operand type(s) for +: 'int' and 'str',说明+不可用于不同类型的变量
a,b,c='张三'
print(a,b,c)
a,b,c='张三','lisi'
print(a,b,c)  #line8/10报错一样，但是原理不同，line8是一个字符串，长度为2，所以got 2（此时python对字符串进行了自动拆包）；line10是定义了两个值，所以也是got 2
a,b,c='三'
print(a,b,c)  #此时报错就变成了got 1
e={1}
print(e*7)  #TypeError: unsupported operand type(s) for *: 'set' and 'int',说明乘法*不能用在数列set
f={'g':1}
print(f*7)  #TypeError: unsupported operand type(s) for *: 'dict' and 'int',说明乘法*不能用在dict
print(int('3.14')) #ValueError: invalid literal for int() with base 10: '3.14'，int() 只能把“纯整数格式”的字符串转成整数
print(int(3.14)) #不会报错，3.14 是一个 浮点数。Python 允许你把浮点数转成整数，规则是 直接截断小数部分。
