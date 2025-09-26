#immutable object
x=10    #integer
print(x,id(x),type(x))  
j,k,l=1,2,3  #特别注意，python里不允许一个语句中出现两个赋值，所以这里不能写成j=1,k=2,l=3的形式，会报错
print(j,k,l)  #打包packing和解包UNpacking的本质是有序序列，所以可以用tuple和list，但是不能用set
j=k=l=1  #链式赋值chained assignment
print(j,k,l)
x=12.1  #float
print(x,id(x),type(x))  #每当重定义一次数字变量，原数字进回收站，再次print只有新数字，没有原数字
y=10
print(y,id(y))  #所谓不可变是指，对象本身的值不能改变，xy只是变量的名字（引用），它随时可以指向别的对象
p=1000
q=1000
print(p,q,id(p),id(q))
z=2+3j  #complex
print(z,id(z),type(z))  #这里需要注意，和数学上习惯使用i表示虚数不同，python里用j表示
y='hello'
print(y,id(y),type(y))  #string
y='world'
print(y,id(y))  #每当重定义一次字符变量，原字符进回收站，再次print只有新字符，没有原字符
tuple=('spring',"summer",'autumn','winter')  #元组里面的元素如果是字符串，需要加引号
print(tuple,id(tuple),type(tuple))
print(tuple[0])  #这里很反直觉，python的索引是从0开始的
tuple=(1,2,3)
print(tuple,type(tuple))
bool=True  #boolean
print(bool,id(bool),type(bool))
print(True+True)
print(False+False)  #bool中，True=1，False=0
fs=frozenset([3,3,2,1])  #这里需要注意，frozenset似乎是一个直接写在括号前的格式，不能直接使用格式名称=来练习，否则会报错为<class 'type'>
print(fs,id(fs),type(fs))  #frozenset()可以冻结list/tuple/set
b=bytes(5)
print(b,type(b))
#mutable object
list=[1,2]  #list
print(list,id(list),type(list))
list.append(3)  #list要在末尾增加元素，使用.append()
print(list,id(list))
list.extend([4,5])  #使用extend(iterable)操作时，它把iterable里面的每个元素展开，依次添加到列表末尾
print(list)  #必须注意，extend操作一次只能接受一个参数，所以多个元素必须用[]括起来
list=[2,3,4]
print(list,id(list))  #每当重定义一次列表变量，原列表进回收站，再次print只有新列表，没有原列表
dict={'a':1,'b':2}  #dictionary存储使用的是key:value对模式，与=的赋值模式不同
print(dict,id(dict),type(dict))
print(dict['a'])  #dict中要通过键调用值，需要使用[' ']结构
dict['c']=3  #dict要增加元素，使用[' ']
print(dict,id(dict))
dict={'a':1,'b':2,'d':3}
print(dict,id(dict))  #每当重定义一次字典变量，原字典进回收站，再次print只有新字典，没有原字典
set={1,2,3,3,2,1}
print(set,id(set),type(set))  #set会去重
set.add(4)
print(set)  #add添加元素
4 in set  #in查找元素，这是一个bool表达式，返回true或false
print(4 in set)