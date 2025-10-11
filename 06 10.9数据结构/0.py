n = 1                    # 全局变量 n

def add(n):              # 参数 n - 这是局部变量，与全局 n 同名但不是同一个
    print(f"函数内修改前: {id(n)}")  # 查看内存地址
    n = n + 1
    print(f"函数内修改后: {id(n)}")  # 地址变了，说明创建了新对象
    return n

print(f"全局n初始地址: {id(n)}")
n = add(n)               # 把返回值赋给全局 n
print(f"全局n最终地址: {id(n)}")



