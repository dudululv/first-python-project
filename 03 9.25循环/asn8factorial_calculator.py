# 阶乘计算器：计算n!，其中n在3到15之间

# 获取并验证用户输入的n值
while True:
    try:
        # 获取用户输入
        n = int(input("请输入一个整数n (3-15之间): "))
        
        # 验证输入范围
        if 3 <= n <= 15:
            break
        else:
            print("输入不满足条件！请输入3到15之间的整数。")
    except ValueError:
        print("无效输入！请输入一个有效的整数。")

# 计算阶乘
factorial = 1
for i in range(1, n + 1):
    factorial *= i

# 输出结果
print(f"{n}的阶乘是: {factorial}")