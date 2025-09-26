j,k,l=1,2,3
print(j+k)
f,g='abc','def'
print(f+g)  #加法+可用于字符串，起到拼接concatenate的作用
f,g,h=(1,2,3),(4,5,6),(1,4,6)
print(f+g+h)  #+用于tuple，多个元组元素按顺序合并为一个tuple
f,g,h=[1,2,3],[4,5,6],[1,4,6]
print(g+f+h)  #+用于list，多个list按加法顺序合并为一个list
print('='*7)
print(f*7)
print(j*k) #乘法*用在str/tuple/list，不可用于dict和set
print(k**l)  #幂
print(j/k)  
print(l//k)  #取整数
print(l%j)  #取余数
x,y=10,3
x+=y
print(x)
x,y=10,3
x-=y
print(x)
x,y=10,3
x*=y
print(x)
x,y=10,3
x**=y
print(x)
x,y=10,3
x/=y
print(x)
x,y=10,3
x//=y
print(x)
x,y=10,3
x%=y
print(x)
m,n=3,5
print(m>n)
print(m>=n)
print(m<n)
print(m<=n)
print(m==n)
print(m!=n)  #python无法识别<>为不等号
m,n=(1,2),(3,4)
print(m>=n,type(m))
print(m<=n,type(m)) #解释如下
'''
两个元组可以使用 <, <=, >, >= 比较，规则如下：Python 会 逐元素比较，从第一个元素开始。如果对应元素可以比较：
如果第一个元素不同，就根据第一个元素的大小判断整个元组的大小。
如果第一个元素相同，就继续比较下一个元素，直到找到不同的元素。如果所有对应元素都相等，长度更长的元组被认为更大。
'''
p,q=True,False
print(p and q)
print(p or q)
print(not q)  #在python中, 非0数字、非空字符串、列表、元组、字典、集合即为True,反之为False
print(bool(0),bool(1),id(1))
u,i=8,9
print(u and i)  #and返回为第一个false的值，如果都为true则返回最后一个true
print(u or i)  #or返回第一个true的值，如果都为false，则返回最后一个false
a=[1,2,3]
b='hello'
print(4 not in a)  #成员运算符
print('h' in b)  #自动解包，严格来说，Python 并不会“自动解包”字符串，而是根据迭代或赋值操作来发生“拆分行为”
e=('zhangsan','lisi')
print('zhang' in e) #这说明元组里面的每一项就是最小元素，不能继续拆分了
c=[1,2]
d=[1,2]
e=c
print(c is d)
print(id(c),id(d))
c,d=1,1
print(c is d)
c,d=999,999
print(c is d)
c='hello'
d='hello'
print(c is d)
print(type(c))
c,d=[],[]
print(c is d)
c,d={},{}
print(c is d)
c,d=(),()
print(c is d)
print(type(c))
c,d=(1),(1)
print(c is d)
print(type(c))
c,d=(1,2),(1,2)
print(c is d)
print(type(c))  #也就是说，不可变对象相同，地址一致，而可变对象即使完全一样，即使是空list和空set，地址也不一致
c=d={1}
print(c is d)  #此时结果相等，说明使用链式法则，可以把可变对象的地址强行变一致
a=input('please enter a number')
b=input('please enter another number')
print(a+b)
a=int(input("enter number1:"))
b=int(input("enter number2:"))
print(a+b)
a=input(g) #此处会报错，因为使用的g在之前无定义。虽然说input函数会将所有的内容使用str函数字符化，但是在进行这一过程之前会先查找g值，如果想要不报错，要么＋引号，要么先进行定义
print(a) 